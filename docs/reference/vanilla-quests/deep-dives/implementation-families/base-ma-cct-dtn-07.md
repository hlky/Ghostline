# base-ma-cct-dtn-07

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_07\community\ma_cct_dtn_07_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_07\ma_cct_dtn_07.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_07\ma_cct_dtn_07.quest` | content candidate | 1 / 0 | base\quest\additional_game_elements.questphase |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_07\ma_cct_dtn_07_phase.questphase` | content candidate | 10 / 0 | base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_07\scene\ma_cct_dtn_07_brief.scene |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_07\scene\ma_cct_dtn_07_brief.scene` | content candidate | 0 / 22 |  |
| `base\quest\bugfixing\minor_quests\ma_cct_dtn_07\ma_cct_dtn_07_quest_bugfixes.questphase` | repair | 2 / 0 |  |

## Journal paths observed in these resources

- `contacts/regina_jones/ma_cct_dtn_07/00_msg_intro`
- `contacts/regina_jones/ma_cct_dtn_07/00_msg_start`
- `contacts/regina_jones/ma_cct_dtn_07/01_ch_info`
- `contacts/regina_jones/ma_cct_dtn_07/01_ch_info/01_ch_info`
- `contacts/regina_jones/ma_cct_dtn_07/01_ch_info_lethal`
- `contacts/regina_jones/ma_cct_dtn_07/01_ch_info_lethal/01_ch_info_lethal`
- `contacts/regina_jones/ma_cct_dtn_07/02_msg_regina`
- `contacts/regina_jones/ma_cct_dtn_07/02_msg_regina_lethal`
- `onscreens/emails/quests/minor_activities/city_center/downtown/ma_cct_dtn_07/onscreens/ma_cct_dtn__07_shard_02`
- `points_of_interest/minor_quests/ma_cct_dtn_07`
- `quests/minor_quest/ma_cct_dtn_07`
- `quests/minor_quest/ma_cct_dtn_07/description`
- `quests/minor_quest/ma_cct_dtn_07/ma_cct_dtn_07/check_shard`
- `quests/minor_quest/ma_cct_dtn_07/ma_cct_dtn_07/clues`
- `quests/minor_quest/ma_cct_dtn_07/ma_cct_dtn_07/find_psycho`
- `quests/minor_quest/ma_cct_dtn_07/ma_cct_dtn_07/find_psycho/area`
- `quests/minor_quest/ma_cct_dtn_07/ma_cct_dtn_07/find_psycho/area_2`
- `quests/minor_quest/ma_cct_dtn_07/ma_cct_dtn_07/kill_psycho`
- `quests/minor_quest/ma_cct_dtn_07/ma_cct_dtn_07/send_info`
- `quests/minor_quest/ma_cct_dtn_07/ma_cct_dtn_07/send_info/contact`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioMixNodeType]` | 11 |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_Kill,questCharacterManagerCombat_NodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 5 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 2 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 4 |
| `questCheckpointNodeDefinition` | 2 |
| `questCombatNodeDefinition` | 5 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 10 |
| `questCombatNodeDefinition[questCombatNodeParams_LookAtTarget]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition,questPhoneMuted_ConditionType,questSystemCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam,questLogicalCondition]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition]` | 1 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 5 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryVisited_ConditionType]` | 1 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 6 |
| `questCutControlNodeDefinition` | 6 |
| `questDeletionMarkerNodeDefinition` | 7 |
| `questEventManagerNodeDefinition` | 12 |
| `questFXManagerNodeDefinition[questPlayFX_NodeType,questPlayFX_NodeTypeParams]` | 4 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 23 |
| `questInputNodeDefinition` | 12 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 2 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 28 |
| `questLogicalAndNodeDefinition` | 2 |
| `questLogicalHubNodeDefinition` | 10 |
| `questLogicalXorNodeDefinition` | 5 |
| `questMappinManagerNodeDefinition` | 2 |
| `questMiscAICommandNode` | 3 |
| `questMiscAICommandNode[questCombatNodeParams_RestrictMovementToArea]` | 1 |
| `questMovePuppetNodeDefinition` | 1 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 2 |
| `questOutputNodeDefinition` | 11 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questLogicalCondition,questSystemCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterAttack_ConditionType,questCharacterCondition]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHealth_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 5 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 5 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 7 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 9 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 3 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryVisited_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questUICondition,questUIElement_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questObjectCondition,questScan_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 24 |
| `questPauseConditionNodeDefinition[questSensesCondition,questVision_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 16 |
| `questPhaseNodeDefinition` | 9 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 2 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 10 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 1 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 1 |
| `questVoicesetManagerNodeDefinition[questChangeVoicesetState_NodeType,questChangeVoicesetState_NodeTypeParams]` | 4 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 8 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 7 |
| `scnCutControlNode[scnNodeId]` | 1 |
| `scnDeletionMarkerNode[scnNodeId]` | 1 |
| `scnEndNode[scnNodeId]` | 2 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 1 |
| `scnStartNode[scnNodeId]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `29c7ac4763cf8bc766bd` | 8 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_07\ma_cct_dtn_07_phase.questphase` / h858 / 7 -> 3 -> 4 |
| `8c7beb1704f04b204046` | 8 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_07\ma_cct_dtn_07_phase.questphase` / h858 / 4 -> 5 -> 6 |
| `ee4b344701c562aa4943` | 8 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_07\ma_cct_dtn_07_phase.questphase` / h858 / 3 -> 4 -> 5 |
| `6b1f06641875683cc2c7` | 5 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_07\ma_cct_dtn_07_phase.questphase` / h1216 / 41 -> 42 -> 37 |
| `754bb5014790dc669c0d` | 4 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_07\ma_cct_dtn_07_phase.questphase` / h0 / 143 -> 153 -> 142 |
| `815c1815268f980fb912` | 4 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_07\ma_cct_dtn_07_phase.questphase` / h858 / 0 -> 8 -> 7 |
| `a909c836470d2b0e7fbc` | 3 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_07\ma_cct_dtn_07_phase.questphase` / h858 / 0 -> 11 -> 1 |
| `bb5f35239f984c46ce98` | 3 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_07\ma_cct_dtn_07_phase.questphase` / h0 / 151 -> 142 -> 144 |
| `0e0b0ec1add4154b2d49` | 2 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_07\ma_cct_dtn_07_phase.questphase` / h0 / 207 -> 208 -> 210 |
| `131b32350d75ba8b8bfe` | 2 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_07\scene\ma_cct_dtn_07_brief.scene` / scene / 430 -> 410 -> 416 |
| `1814642825aef5741f77` | 2 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_07\ma_cct_dtn_07_phase.questphase` / h0 / 151 -> 142 -> 150 |
| `18be198845c90c6bb3c8` | 2 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_07\ma_cct_dtn_07_phase.questphase` / h202 / 5 -> 10 -> 6 |
| `256f5695ecda8ef528d7` | 2 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_07\ma_cct_dtn_07_phase.questphase` / h0 / 182 -> 183 -> 17 |
| `2e1ee5a1324dbeeb9071` | 2 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_07\ma_cct_dtn_07_phase.questphase` / h1859 / 2 -> 4 -> 8 |
| `3e6f03030764fcc75954` | 2 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_07\ma_cct_dtn_07_phase.questphase` / h0 / 142 -> 144 -> 143 |
| `3f741c34ad3c83a225f1` | 2 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_07\ma_cct_dtn_07_phase.questphase` / h1216 / 0 -> 132 -> 192 |
| `81a794c3e5b42ff8dfb0` | 2 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_07\ma_cct_dtn_07_phase.questphase` / h606 / 17 -> 6 -> 1 |
| `8b7c7b83f17e24f841e8` | 2 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_07\ma_cct_dtn_07_phase.questphase` / h0 / 208 -> 210 -> 218 |
| `8dd3932a10644218e399` | 2 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_07\ma_cct_dtn_07_phase.questphase` / h0 / 144 -> 143 -> 153 |
| `ac5b347c9518873a2790` | 2 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_07\scene\ma_cct_dtn_07_brief.scene` / scene / 410 -> 416 -> 414 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
