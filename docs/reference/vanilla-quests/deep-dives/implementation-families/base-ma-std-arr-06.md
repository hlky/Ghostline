# base-ma-std-arr-06

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\community\ma_std_arr_06_com_homeless.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\community\ma_std_arr_06_com_psycho.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\ma_std_arr_06.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\ma_std_arr_06.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\ma_std_arr_06_phase.questphase; base\open_world\phases\open_world_content.questphase |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\ma_std_arr_06_phase.questphase` | content candidate | 8 / 0 | base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\scenes\ma_std_arr_06_briefing.scene |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\scenes\ma_std_arr_06_briefing.scene` | content candidate | 0 / 22 |  |
| `base\quest\bugfixing\minor_quests\ma_std_arr_06\ma_std_arr_06_quest_bugfixes.questphase` | repair | 3 / 0 |  |

## Journal paths observed in these resources

- `contacts/regina_jones/ma_std_arr_06/00_msg_rejected_call`
- `contacts/regina_jones/ma_std_arr_06/00_msg_start`
- `contacts/regina_jones/ma_std_arr_06/01_ch_info/01_ch_info`
- `contacts/regina_jones/ma_std_arr_06/01_ch_info/01_ch_info_killed`
- `contacts/regina_jones/ma_std_arr_06/02_msg_regina`
- `contacts/regina_jones/ma_std_arr_06/02_msg_regina_killed`
- `onscreens/emails/quests/minor_activities/santo_domingo/arroyo/ma_std_arr_06/onscreens/ma_std_arr_06_onscreen_01`
- `onscreens/emails/quests/minor_activities/santo_domingo/arroyo/ma_std_arr_06/onscreens/ma_std_arr_06_onscreen_02`
- `points_of_interest/minor_activities/ma_std_arr_06`
- `points_of_interest/minor_quests/ma_std_arr_06`
- `quests/minor_quest/ma_std_arr_06`
- `quests/minor_quest/ma_std_arr_06/ma_description`
- `quests/minor_quest/ma_std_arr_06/ma_std_arr_06/check_shard`
- `quests/minor_quest/ma_std_arr_06/ma_std_arr_06/clues`
- `quests/minor_quest/ma_std_arr_06/ma_std_arr_06/clues/area`
- `quests/minor_quest/ma_std_arr_06/ma_std_arr_06/clues/area1`
- `quests/minor_quest/ma_std_arr_06/ma_std_arr_06/find_psycho`
- `quests/minor_quest/ma_std_arr_06/ma_std_arr_06/find_psycho/turret_01`
- `quests/minor_quest/ma_std_arr_06/ma_std_arr_06/find_psycho/turret_02`
- `quests/minor_quest/ma_std_arr_06/ma_std_arr_06/kill_psycho`
- `quests/minor_quest/ma_std_arr_06/ma_std_arr_06/send_info`
- `quests/minor_quest/ma_std_arr_06/ma_std_arr_06/send_info/contact`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioMixNodeType]` | 9 |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_Kill,questCharacterManagerCombat_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition,questPhoneMuted_ConditionType,questSystemCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 5 |
| `questConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition]` | 1 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 3 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryVisited_ConditionType]` | 1 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 4 |
| `questCutControlNodeDefinition` | 1 |
| `questDeletionMarkerNodeDefinition` | 10 |
| `questEventManagerNodeDefinition` | 3 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 24 |
| `questInputNodeDefinition` | 11 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_ActionProperty,questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 2 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 2 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 3 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 22 |
| `questLogicalAndNodeDefinition` | 1 |
| `questLogicalHubNodeDefinition` | 3 |
| `questLogicalXorNodeDefinition` | 6 |
| `questMappinManagerNodeDefinition` | 6 |
| `questMiscAICommandNode` | 1 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 1 |
| `questOutputNodeDefinition` | 9 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questLogicalCondition,questSystemCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHealth_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 6 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 4 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 4 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryVisited_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questUICondition,questUIElement_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questObjectCondition,questScan_ConditionType]` | 7 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 7 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 13 |
| `questPhaseNodeDefinition` | 10 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questPuppetAIManagerNodeDefinition[questPuppetAIManagerNodeDefinitionEntry]` | 2 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 9 |
| `questStartNodeDefinition` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 1 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 3 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 4 |
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
| `caba80ba05338541aa18` | 3 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\ma_std_arr_06_phase.questphase` / h0 / 166 -> 208 -> 194 |
| `d3bf86a2bbb84d894747` | 3 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\ma_std_arr_06_phase.questphase` / h75 / 9 -> 2 -> 3 |
| `131b32350d75ba8b8bfe` | 2 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\scenes\ma_std_arr_06_briefing.scene` / scene / 280 -> 262 -> 268 |
| `18be198845c90c6bb3c8` | 2 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\ma_std_arr_06_phase.questphase` / h75 / 5 -> 10 -> 6 |
| `251a2e228d9287a906fd` | 2 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\ma_std_arr_06_phase.questphase` / h1075 / 7 -> 2 -> 3 |
| `256f5695ecda8ef528d7` | 2 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\ma_std_arr_06_phase.questphase` / h0 / 319 -> 320 -> 186 |
| `3783015b6f4c1f41b1ac` | 2 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\ma_std_arr_06_phase.questphase` / h0 / 216 -> 217 -> 236 |
| `5c36562b0d3ec0c3ad85` | 2 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\ma_std_arr_06_phase.questphase` / h0 / 208 -> 194 -> 210 |
| `9af8a87f20a910659fa8` | 2 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\ma_std_arr_06_phase.questphase` / h0 / 229 -> 199 -> 200 |
| `9e91b012f1a515523726` | 2 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\ma_std_arr_06_phase.questphase` / h0 / 217 -> 218 -> 231 |
| `a19ded5c23821bd7e0ab` | 2 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\ma_std_arr_06_phase.questphase` / h1075 / 13 -> 7 -> 2 |
| `a5ba871bf92eb584e50a` | 2 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\ma_std_arr_06_phase.questphase` / h0 / 166 -> 208 -> 207 |
| `ac5b347c9518873a2790` | 2 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\scenes\ma_std_arr_06_briefing.scene` / scene / 262 -> 268 -> 266 |
| `b1ff4db30ad594857e2e` | 2 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\ma_std_arr_06_phase.questphase` / h989 / 5 -> 12 -> 13 |
| `b4a0ea15fadec3bacd08` | 2 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\ma_std_arr_06_phase.questphase` / h0 / 217 -> 236 -> 231 |
| `bbf9efd740881cf31a37` | 2 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\scenes\ma_std_arr_06_briefing.scene` / scene / 277 -> 280 -> 262 |
| `cb342d602e28e6bfccc1` | 2 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\ma_std_arr_06_phase.questphase` / h0 / 224 -> 256 -> 281 |
| `d6b7c21f5d2d0ab76fc6` | 2 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\scenes\ma_std_arr_06_briefing.scene` / scene / 120 -> 121 -> 6 |
| `e5742f9794e6583c67cb` | 2 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\scenes\ma_std_arr_06_briefing.scene` / scene / 125 -> 120 -> 121 |
| `f1cab9108d90f7f5b3df` | 2 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\ma_std_arr_06_phase.questphase` / h0 / 226 -> 235 -> 228 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
