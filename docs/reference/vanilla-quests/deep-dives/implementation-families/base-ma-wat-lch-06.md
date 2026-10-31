# base-ma-wat-lch-06

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_06\community\ma_wat_lch_06_after_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_06\community\ma_wat_lch_06_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_06\ma_wat_lch_06.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_06\ma_wat_lch_06.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\watson\little_china\ma_wat_lch_06\test\ma_wat_lch_06_chicken_test.scene; base\quest\additional_game_elements.questphase |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_06\phases\ma_wat_lch_06_phase.questphase` | content candidate | 9 / 0 | base\open_world\minor_activities\watson\little_china\ma_wat_lch_06\scenes\ma_wat_lch_06_brief.scene; base\open_world\minor_activities\watson\little_china\ma_wat_lch_06\scenes\ma_wat_lch_06_clues_n_mood.scene |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_06\scenes\ma_wat_lch_06_brief.scene` | content candidate | 0 / 22 |  |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_06\scenes\ma_wat_lch_06_clues_n_mood.scene` | content candidate | 0 / 10 |  |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_06\test\ma_wat_lch_06_chicken_test.scene` | test/debug | 0 / 4 |  |
| `base\quest\bugfixing\minor_quests\ma_wat_lch_06\ma_wat_lch_06_quest_bugfixes.questphase` | repair | 2 / 0 |  |

## Journal paths observed in these resources

- `contacts/regina_jones/ma_wat_lch_06/00_msg_intro`
- `contacts/regina_jones/ma_wat_lch_06/00_msg_start`
- `contacts/regina_jones/ma_wat_lch_06/01_ch_info`
- `contacts/regina_jones/ma_wat_lch_06/01_ch_info/01_ch_info`
- `contacts/regina_jones/ma_wat_lch_06/01_ch_info_lethal`
- `contacts/regina_jones/ma_wat_lch_06/01_ch_info_lethal/01_ch_info_lethal`
- `contacts/regina_jones/ma_wat_lch_06/02_msg_regina`
- `contacts/regina_jones/ma_wat_lch_06/02_msg_regina_lethal`
- `onscreens/emails/quests/minor_activities/watson/little_china/ma_wat_lch_06/onscreens/ma_wat_lch_06_1`
- `onscreens/emails/quests/minor_activities/watson/little_china/ma_wat_lch_06/onscreens/ma_wat_lch_06_3`
- `onscreens/emails/quests/minor_activities/watson/little_china/ma_wat_lch_06/onscreens/ma_wat_lch_06_4`
- `points_of_interest/minor_quests/ma_wat_lch_06`
- `quests/minor_quest/ma_wat_lch_06`
- `quests/minor_quest/ma_wat_lch_06/description`
- `quests/minor_quest/ma_wat_lch_06/ma_wat_lch_06/check_shard`
- `quests/minor_quest/ma_wat_lch_06/ma_wat_lch_06/check_shard_partner`
- `quests/minor_quest/ma_wat_lch_06/ma_wat_lch_06/clues`
- `quests/minor_quest/ma_wat_lch_06/ma_wat_lch_06/find_psycho`
- `quests/minor_quest/ma_wat_lch_06/ma_wat_lch_06/kill_psycho`
- `quests/minor_quest/ma_wat_lch_06/ma_wat_lch_06/send_info`
- `quests/minor_quest/ma_wat_lch_06/ma_wat_lch_06/send_info/contact`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioMixNodeType]` | 9 |
| `questCheckpointNodeDefinition` | 2 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 1 |
| `questCombatNodeDefinition[questCombatNodeParams_SecondaryWeapon]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition,questPhoneMuted_ConditionType,questSystemCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition]` | 2 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryVisited_ConditionType]` | 2 |
| `questCutControlNodeDefinition` | 4 |
| `questDeletionMarkerNodeDefinition` | 5 |
| `questEventManagerNodeDefinition` | 10 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 22 |
| `questInputNodeDefinition` | 11 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 1 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 22 |
| `questLogicalAndNodeDefinition` | 4 |
| `questLogicalHubNodeDefinition` | 8 |
| `questLogicalXorNodeDefinition` | 7 |
| `questMiscAICommandNode` | 2 |
| `questMiscAICommandNode[questCombatNodeParams_RestrictMovementToArea]` | 3 |
| `questMovePuppetNodeDefinition[questMoveToParams,questUniversalRef]` | 2 |
| `questOutputNodeDefinition` | 8 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questSystemCondition,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questLogicalCondition,questSystemCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterAttack_ConditionType,questCharacterCondition]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHealth_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 6 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 6 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 2 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 5 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryVisited_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questUICondition,questUIElement_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questObjectCondition,questScan_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 17 |
| `questPauseConditionNodeDefinition[questSensesCondition,questVision_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 12 |
| `questPhaseNodeDefinition` | 10 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 3 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 4 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questTransformAnimatorNodeDefinition[questTransformAnimatorNode_Action_Play]` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 1 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 2 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 7 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 3 |
| `scnChoiceNode[scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnCutControlNode[scnNodeId]` | 1 |
| `scnDeletionMarkerNode[scnNodeId]` | 1 |
| `scnEndNode[scnNodeId]` | 4 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 2 |
| `scnStartNode[scnNodeId]` | 3 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `29c7ac4763cf8bc766bd` | 6 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_06\phases\ma_wat_lch_06_phase.questphase` / h1116 / 7 -> 3 -> 4 |
| `8c7beb1704f04b204046` | 6 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_06\phases\ma_wat_lch_06_phase.questphase` / h1116 / 4 -> 5 -> 6 |
| `ee4b344701c562aa4943` | 6 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_06\phases\ma_wat_lch_06_phase.questphase` / h1116 / 3 -> 4 -> 5 |
| `754bb5014790dc669c0d` | 4 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_06\phases\ma_wat_lch_06_phase.questphase` / h0 / 126 -> 138 -> 125 |
| `815c1815268f980fb912` | 3 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_06\phases\ma_wat_lch_06_phase.questphase` / h1116 / 0 -> 8 -> 7 |
| `bb5f35239f984c46ce98` | 3 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_06\phases\ma_wat_lch_06_phase.questphase` / h0 / 136 -> 125 -> 127 |
| `001cc57b9d7757983c95` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_06\phases\ma_wat_lch_06_phase.questphase` / h0 / 114 -> 90 -> 113 |
| `0d4d0dac270dc158e66a` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_06\phases\ma_wat_lch_06_phase.questphase` / h0 / 7 -> 53 -> 49 |
| `131b32350d75ba8b8bfe` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_06\scenes\ma_wat_lch_06_brief.scene` / scene / 410 -> 415 -> 421 |
| `1814642825aef5741f77` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_06\phases\ma_wat_lch_06_phase.questphase` / h0 / 136 -> 125 -> 135 |
| `21a735d428abaea4a228` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_06\phases\ma_wat_lch_06_phase.questphase` / h0 / 146 -> 147 -> 148 |
| `240148efc76953d1c5d4` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_06\phases\ma_wat_lch_06_phase.questphase` / h0 / 147 -> 148 -> 149 |
| `3e6f03030764fcc75954` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_06\phases\ma_wat_lch_06_phase.questphase` / h0 / 125 -> 127 -> 126 |
| `8bd54738c2c85f70192e` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_06\phases\ma_wat_lch_06_phase.questphase` / h0 / 11 -> 12 -> 13 |
| `8dd3932a10644218e399` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_06\phases\ma_wat_lch_06_phase.questphase` / h0 / 127 -> 126 -> 138 |
| `9d3905de8dc6095eec1b` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_06\phases\ma_wat_lch_06_phase.questphase` / h1175 / 13 -> 14 -> 8 |
| `a82067221743e1f7d73f` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_06\phases\ma_wat_lch_06_phase.questphase` / h1175 / 14 -> 8 -> 7 |
| `a909c836470d2b0e7fbc` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_06\phases\ma_wat_lch_06_phase.questphase` / h1116 / 0 -> 11 -> 1 |
| `ac5b347c9518873a2790` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_06\scenes\ma_wat_lch_06_brief.scene` / scene / 415 -> 421 -> 419 |
| `bbf9efd740881cf31a37` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_06\scenes\ma_wat_lch_06_brief.scene` / scene / 408 -> 410 -> 415 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
