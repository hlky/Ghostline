# base-ma-hey-spr-04

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\community\ma_hey_spr_04_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\ma_hey_spr_04.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\ma_hey_spr_04.quest` | content candidate | 2 / 0 | base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\ma_hey_spr_04_phase.questphase; base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\test\ma_hey_spr_04_00_chickentest.scene; base\quest\additional_game_elements.questphase |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\ma_hey_spr_04_phase.questphase` | content candidate | 5 / 0 | base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\scenes\ma_hey_spr_04_01a_briefing.scene; base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\scenes\may_hey_spr_04_01_exposition.scene |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\scenes\ma_hey_spr_04_01a_briefing.scene` | content candidate | 0 / 22 |  |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\scenes\may_hey_spr_04_01_exposition.scene` | content candidate | 0 / 14 |  |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\test\ma_hey_spr_04_00_chickentest.scene` | test/debug | 0 / 3 |  |
| `base\quest\bugfixing\minor_quests\ma_hey_spr_04\ma_hey_spr_04_quest_bugfixes.questphase` | repair | 2 / 0 |  |

## Journal paths observed in these resources

- `contacts/regina_jones/ma_hey_spr_04/00_msg_intro`
- `contacts/regina_jones/ma_hey_spr_04/00_msg_start`
- `contacts/regina_jones/ma_hey_spr_04/01_ch_info`
- `contacts/regina_jones/ma_hey_spr_04/03_msg_conclusion`
- `contacts/regina_jones/ma_hey_spr_04/03a_ch_alive`
- `contacts/regina_jones/ma_hey_spr_04/03a_ch_alive/03a_ch_alive`
- `contacts/regina_jones/ma_hey_spr_04/03b_ch_dead`
- `contacts/regina_jones/ma_hey_spr_04/03b_ch_dead/03b_ch_dead`
- `contacts/regina_jones/ma_hey_spr_04/04_msg_conclusion`
- `contacts/regina_jones/ma_hey_spr_04/04b_msg_conclusion_dead`
- `onscreens/emails/quests/minor_activities/heywood/wellsprings/ma_hey_spr_04/onscreens/ma_hey_spr_04_shard_producer`
- `onscreens/emails/quests/minor_activities/heywood/wellsprings/ma_hey_spr_04/onscreens/ma_hey_spr_04_shard_psycho`
- `onscreens/emails/quests/minor_activities/heywood/wellsprings/ma_hey_spr_04/onscreens/ma_hey_spr_04_shard_sister`
- `points_of_interest/minor_quests/ma_hey_spr_04`
- `quests/minor_quest/ma_hey_spr_04`
- `quests/minor_quest/ma_hey_spr_04/ma_decription`
- `quests/minor_quest/ma_hey_spr_04/ma_hey_spr_04/find_psycho`
- `quests/minor_quest/ma_hey_spr_04/ma_hey_spr_04/kill_psycho`
- `quests/minor_quest/ma_hey_spr_04/ma_hey_spr_04/loot_psycho`
- `quests/minor_quest/ma_hey_spr_04/ma_hey_spr_04/read_shard_producer`
- `quests/minor_quest/ma_hey_spr_04/ma_hey_spr_04/read_shard_producer1`
- `quests/minor_quest/ma_hey_spr_04/ma_hey_spr_04/read_shard_psycho`
- `quests/minor_quest/ma_hey_spr_04/ma_hey_spr_04/search_clues`
- `quests/minor_quest/ma_hey_spr_04/ma_hey_spr_04/send_info`
- `quests/minor_quest/ma_hey_spr_04/ma_hey_spr_04/send_info/reggie`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioEventNodeType]` | 7 |
| `questAudioNodeDefinition[questAudioMixNodeType]` | 6 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetProgressionBuild]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 1 |
| `questCheckpointNodeDefinition` | 3 |
| `questCombatNodeDefinition` | 2 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 2 |
| `questCombatNodeDefinition[questCombatNodeParams_PrimaryWeapon]` | 1 |
| `questCombatNodeDefinition[questCombatNodeParams_SecondaryWeapon]` | 1 |
| `questCombatNodeDefinition[questCombatNodeParams_UseCover]` | 1 |
| `questConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition,questPhoneMuted_ConditionType,questSystemCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition]` | 2 |
| `questConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 4 |
| `questCutControlNodeDefinition` | 2 |
| `questDeletionMarkerNodeDefinition` | 11 |
| `questEndNodeDefinition` | 1 |
| `questEnvironmentManagerNodeDefinition[questPlayEnv_SetWeather]` | 5 |
| `questEventManagerNodeDefinition` | 11 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 31 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 3 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 1 |
| `questInputNodeDefinition` | 8 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 3 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 27 |
| `questLogicalAndNodeDefinition` | 3 |
| `questLogicalHubNodeDefinition` | 15 |
| `questLogicalXorNodeDefinition` | 5 |
| `questMiscAICommandNode` | 1 |
| `questMiscAICommandNode[questCombatNodeParams_RestrictMovementToArea]` | 2 |
| `questMovePuppetNodeDefinition[questMoveToParams,questUniversalRef]` | 1 |
| `questOutputNodeDefinition` | 7 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questSystemCondition,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questLogicalCondition,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterAim_ConditionType,questCharacterCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHealth_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questTriggerCondition,questVarComparison_ConditionType]` | 4 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 7 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 2 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryVisited_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questObjectCondition,questScan_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 11 |
| `questPauseConditionNodeDefinition[questSensesCondition,questStimuli_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questSensesCondition,questVision_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 11 |
| `questPhaseNodeDefinition` | 7 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneNodeDefinition[scnToggleInterruption_InterruptionOperation,scnWorldMarker]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 3 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 3 |
| `questStartNodeDefinition` | 1 |
| `questSwitchNodeDefinition[questConditionItem,questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questTimeManagerNodeDefinition[questSetTime_NodeType]` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 3 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 3 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 2 |
| `scnCutControlNode[scnNodeId]` | 2 |
| `scnDeletionMarkerNode[scnNodeId]` | 1 |
| `scnEndNode[scnNodeId]` | 3 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 5 |
| `scnStartNode[scnNodeId]` | 5 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `9af8a87f20a910659fa8` | 5 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\ma_hey_spr_04_phase.questphase` / h0 / 75 -> 101 -> 102 |
| `0a0df9057e5523d5f8ab` | 3 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\ma_hey_spr_04_phase.questphase` / h0 / 184 -> 135 -> 189 |
| `14f563bd79bb19a59156` | 3 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\ma_hey_spr_04_phase.questphase` / h1155 / 15 -> 30 -> 20 |
| `240148efc76953d1c5d4` | 3 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\ma_hey_spr_04_phase.questphase` / h0 / 124 -> 123 -> 125 |
| `f804f6e892c85460f6d3` | 3 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\ma_hey_spr_04_phase.questphase` / h0 / 49 -> 115 -> 117 |
| `131b32350d75ba8b8bfe` | 2 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\scenes\ma_hey_spr_04_01a_briefing.scene` / scene / 186 -> 189 -> 195 |
| `53989c16dd360838ad98` | 2 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\ma_hey_spr_04_phase.questphase` / h0 / 171 -> 172 -> 173 |
| `a909c836470d2b0e7fbc` | 2 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\ma_hey_spr_04_phase.questphase` / h240 / 0 -> 8 -> 1 |
| `ac5b347c9518873a2790` | 2 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\scenes\ma_hey_spr_04_01a_briefing.scene` / scene / 189 -> 195 -> 193 |
| `b1e67a56061f85fff379` | 2 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\ma_hey_spr_04_phase.questphase` / h0 / 115 -> 117 -> 127 |
| `bbf9efd740881cf31a37` | 2 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\scenes\ma_hey_spr_04_01a_briefing.scene` / scene / 183 -> 186 -> 189 |
| `bd5a6f93c73e722e1e3d` | 2 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\ma_hey_spr_04_phase.questphase` / h0 / 136 -> 49 -> 119 |
| `d6b7c21f5d2d0ab76fc6` | 2 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\scenes\ma_hey_spr_04_01a_briefing.scene` / scene / 132 -> 133 -> 2 |
| `02a5265bcccfc8e3cf77` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\ma_hey_spr_04_phase.questphase` / h658 / 6 -> 9 -> 3 |
| `02f1a1ecc108e1d384e8` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\test\ma_hey_spr_04_00_chickentest.scene` / scene / 1 -> 6 -> 2 |
| `03760988bdf4ff45b31d` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\scenes\may_hey_spr_04_01_exposition.scene` / scene / 20 -> 8 -> 38 |
| `046a104fe6200aa02022` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\ma_hey_spr_04_phase.questphase` / h0 / 275 -> 276 -> 277 |
| `04e49e494ee062430989` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\ma_hey_spr_04_phase.questphase` / h0 / 376 -> 45 -> 109 |
| `05c992f8b920e82f8b9a` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\ma_hey_spr_04_phase.questphase` / h0 / 255 -> 259 -> 257 |
| `066acc9cc0b60d105ef2` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\ma_hey_spr_04_phase.questphase` / h0 / 129 -> 179 -> 255 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
