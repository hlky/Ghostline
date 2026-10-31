# base-ma-wat-kab-02

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\community\ma_wat_kab_02_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\ma_wat_kab_02.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\ma_wat_kab_02_phase.questphase` | content candidate | 9 / 0 | base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\scenes\ma_wat_kab_02.scene |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\ma_wat_kab_02_quest.quest` | content candidate | 1 / 0 | base\open_world\phases\open_world_content.questphase; base\quest\additional_game_elements.questphase |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\scenes\ma_wat_kab_02.scene` | content candidate | 0 / 76 |  |
| `base\quest\bugfixing\minor_quests\ma_wat_kab_02\ma_wat_kab_02_quest_bugfixes.questphase` | repair | 3 / 0 |  |

## Journal paths observed in these resources

- `contacts/regina_jones/ma_wat_kab_02/000_hook`
- `contacts/regina_jones/ma_wat_kab_02/00_msg_start`
- `contacts/regina_jones/ma_wat_kab_02/01_ch_info`
- `contacts/regina_jones/ma_wat_kab_02/01_ch_info/01_ch_info`
- `contacts/regina_jones/ma_wat_kab_02/01_ch_info_killed`
- `contacts/regina_jones/ma_wat_kab_02/01_ch_info_killed/01_ch_info_killed`
- `contacts/regina_jones/ma_wat_kab_02/02_msg_regina`
- `contacts/regina_jones/ma_wat_kab_02/02_msg_regina_killed`
- `onscreens/emails/quests/minor_activities/watson/kabuki/ma_wat_kab_02/onscreens/ma_wat_kab_02_onscreen_02`
- `points_of_interest/minor_activities/ma_wat_kab_02`
- `points_of_interest/minor_quests/ma_wat_kab_02`
- `quests/minor_quest/ma_wat_kab_02`
- `quests/minor_quest/ma_wat_kab_02/description`
- `quests/minor_quest/ma_wat_kab_02/ma_wat_kab_02/investigate_bridge`
- `quests/minor_quest/ma_wat_kab_02/ma_wat_kab_02/kill_psycho`
- `quests/minor_quest/ma_wat_kab_02/ma_wat_kab_02/search_clues`
- `quests/minor_quest/ma_wat_kab_02/ma_wat_kab_02/search_clues/laptop`
- `quests/minor_quest/ma_wat_kab_02/ma_wat_kab_02/send_info`
- `quests/minor_quest/ma_wat_kab_02/ma_wat_kab_02/send_info/regina`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioEventNodeType]` | 4 |
| `questAudioNodeDefinition[questAudioMixNodeType]` | 6 |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_Kill,questCharacterManagerCombat_NodeType]` | 3 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 4 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetReactionPreset,questReactionPresetRecordSelector]` | 2 |
| `questCheckpointNodeDefinition` | 2 |
| `questCombatNodeDefinition` | 1 |
| `questConditionNodeDefinition[questCameraFocus_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questSystemCondition,questUniversalRef,questValueDistance]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 2 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition,questPhoneMuted_ConditionType,questSystemCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 5 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition]` | 2 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 1 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 4 |
| `questCutControlNodeDefinition` | 8 |
| `questDeletionMarkerNodeDefinition` | 10 |
| `questEquipItemNodeDefinition[questEquipItemParams,questObservableUniversalRef]` | 2 |
| `questEventManagerNodeDefinition` | 28 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 23 |
| `questInputNodeDefinition` | 12 |
| `questItemManagerNodeDefinition[questUniversalRef,questUseWeapon_NodeType]` | 2 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 9 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 18 |
| `questLogicalAndNodeDefinition` | 2 |
| `questLogicalHubNodeDefinition` | 18 |
| `questLogicalXorNodeDefinition` | 4 |
| `questMappinManagerNodeDefinition` | 1 |
| `questMiscAICommandNode` | 1 |
| `questMovePuppetNodeDefinition` | 1 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 2 |
| `questOutputNodeDefinition` | 12 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectCondition,questObjectDistance,questScan_ConditionType,questSystemCondition,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questLogicalCondition,questSystemCondition,questTriggerCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterAttack_ConditionType,questCharacterCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHealth_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 5 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questFactsDBCondition,questLogicalCondition,questObjectDistance,questUniversalRef,questValueDistance,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 6 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 5 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition,questObjectCondition,questScan_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questRealtimeDelay_ConditionType,questSensesCondition,questTimeCondition,questVision_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questUICondition,questUIElement_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questObjectCondition,questScan_ConditionType]` | 7 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 15 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 17 |
| `questPhaseNodeDefinition` | 11 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questPuppetAIManagerNodeDefinition[questPuppetAIManagerNodeDefinitionEntry]` | 2 |
| `questRandomizerNodeDefinition` | 3 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 2 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 7 |
| `questStartNodeDefinition` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 2 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 3 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 3 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 12 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 13 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsAttachToGameObjectParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 3 |
| `scnCutControlNode[scnNodeId]` | 2 |
| `scnDeletionMarkerNode[scnNodeId]` | 1 |
| `scnEndNode[scnNodeId]` | 4 |
| `scnHubNode[scnNodeId]` | 2 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnRandomizerNode[scnNodeId]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 7 |
| `scnStartNode[scnNodeId]` | 3 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `1e253d0fcbd364975401` | 4 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\ma_wat_kab_02_phase.questphase` / h210 / 10 -> 2 -> 23 |
| `0e8f622afa242001778b` | 3 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\scenes\ma_wat_kab_02.scene` / scene / 219 -> 218 -> 286 |
| `18be198845c90c6bb3c8` | 3 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\ma_wat_kab_02_phase.questphase` / h0 / 31 -> 35 -> 33 |
| `400ab17c1f3363cf36e2` | 3 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\ma_wat_kab_02_phase.questphase` / h0 / 72 -> 261 -> 263 |
| `44fb8ec1826768134e0d` | 3 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\ma_wat_kab_02_phase.questphase` / h0 / 223 -> 263 -> 262 |
| `46832392e10cc5a581d6` | 3 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\ma_wat_kab_02_phase.questphase` / h210 / 14 -> 15 -> 16 |
| `bbf9efd740881cf31a37` | 3 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\scenes\ma_wat_kab_02.scene` / scene / 363 -> 368 -> 182 |
| `cb0f56ab4d623fffef33` | 3 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\ma_wat_kab_02_phase.questphase` / h0 / 278 -> 290 -> 8 |
| `d72a1b8778083ff0e104` | 3 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\ma_wat_kab_02_phase.questphase` / h0 / 222 -> 223 -> 72 |
| `d8f4630d2483415fcde0` | 3 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\ma_wat_kab_02_phase.questphase` / h210 / 7 -> 13 -> 1 |
| `0dc16e049fa28f95b55f` | 2 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\ma_wat_kab_02_phase.questphase` / h0 / 16 -> 17 -> 39 |
| `131b32350d75ba8b8bfe` | 2 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\scenes\ma_wat_kab_02.scene` / scene / 521 -> 503 -> 509 |
| `2d8cfb97ad1389c97795` | 2 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\ma_wat_kab_02_phase.questphase` / h1222 / 23 -> 20 -> 22 |
| `394c7be0fe681bfc1769` | 2 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\scenes\ma_wat_kab_02.scene` / scene / 363 -> 384 -> 398 |
| `43614d3e2db5dc5f8e81` | 2 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\ma_wat_kab_02_phase.questphase` / h1222 / 2 -> 20 -> 22 |
| `438480bd00bff02e0c63` | 2 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\scenes\ma_wat_kab_02.scene` / scene / 377 -> 115 -> 117 |
| `540a8b379cb0607aef4e` | 2 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\ma_wat_kab_02_phase.questphase` / h1222 / 21 -> 2 -> 20 |
| `657c92db345f2266262a` | 2 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\ma_wat_kab_02_phase.questphase` / h1222 / 23 -> 20 -> 24 |
| `694dcc3f01ba46e3e166` | 2 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\ma_wat_kab_02_phase.questphase` / h0 / 233 -> 235 -> 240 |
| `6e3b35557bcc40a5d957` | 2 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\ma_wat_kab_02_phase.questphase` / h0 / 33 -> 41 -> 244 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
