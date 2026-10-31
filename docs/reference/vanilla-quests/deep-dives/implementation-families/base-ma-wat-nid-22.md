# base-ma-wat-nid-22

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_22\community\ma_wat_nid_22.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_22\community\ma_wat_nid_22_fluff.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_22\ma_wat_nid_22.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_22\ma_wat_nid_22.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\watson\northside\ma_wat_nid_22\ma_wat_nid_22_phase.questphase; base\open_world\phases\open_world_content.questphase |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_22\ma_wat_nid_22_phase.questphase` | content candidate | 8 / 0 | base\open_world\minor_activities\watson\northside\ma_wat_nid_22\scenes\ma_wat_nid_22_clues.scene |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_22\scenes\ma_wat_nid_22_clues.scene` | content candidate | 0 / 22 |  |
| `base\quest\bugfixing\minor_quests\ma_wat_nid_22\ma_wat_nid_22_quest_bugfixes.questphase` | repair | 2 / 0 |  |

## Journal paths observed in these resources

- `contacts/regina_jones/ma_wat_nid_22/00_msg_rejected_call`
- `contacts/regina_jones/ma_wat_nid_22/00_msg_start`
- `contacts/regina_jones/ma_wat_nid_22/01_ch_info/01_ch_info`
- `contacts/regina_jones/ma_wat_nid_22/01_ch_info/01_ch_info_killed`
- `contacts/regina_jones/ma_wat_nid_22/02_msg_regina`
- `contacts/regina_jones/ma_wat_nid_22/02_msg_regina_killed`
- `onscreens/emails/quests/minor_activities/watson/norhside_industrial_district/ma_wat_nid_22/onscreens/ma_wat_nid_22_fun`
- `onscreens/emails/quests/minor_activities/watson/norhside_industrial_district/ma_wat_nid_22/onscreens/ma_wat_nid_22_sanity`
- `points_of_interest/minor_quests/ma_wat_nid_22`
- `quests/minor_quest/ma_wat_nid_22`
- `quests/minor_quest/ma_wat_nid_22/description`
- `quests/minor_quest/ma_wat_nid_22/ma_wat_nid_22`
- `quests/minor_quest/ma_wat_nid_22/ma_wat_nid_22/check_shard`
- `quests/minor_quest/ma_wat_nid_22/ma_wat_nid_22/clues`
- `quests/minor_quest/ma_wat_nid_22/ma_wat_nid_22/clues/area`
- `quests/minor_quest/ma_wat_nid_22/ma_wat_nid_22/clues/area1`
- `quests/minor_quest/ma_wat_nid_22/ma_wat_nid_22/find`
- `quests/minor_quest/ma_wat_nid_22/ma_wat_nid_22/kill`
- `quests/minor_quest/ma_wat_nid_22/ma_wat_nid_22/send_info`
- `quests/minor_quest/ma_wat_nid_22/ma_wat_nid_22/send_info/contact`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioMixNodeType]` | 11 |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_Kill,questCharacterManagerCombat_NodeType]` | 2 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 2 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetReactionPreset,questReactionPresetRecordSelector]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 3 |
| `questCheckpointNodeDefinition` | 2 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 2 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition,questPhoneMuted_ConditionType,questSystemCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 4 |
| `questConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition]` | 1 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryVisited_ConditionType]` | 1 |
| `questConditionNodeDefinition[questTriggerCondition]` | 1 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 1 |
| `questCutControlNodeDefinition` | 2 |
| `questDeletionMarkerNodeDefinition` | 15 |
| `questEventManagerNodeDefinition` | 7 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 26 |
| `questInputNodeDefinition` | 10 |
| `questItemManagerNodeDefinition[questUniversalRef,questUseWeapon_NodeType]` | 1 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 22 |
| `questLogicalAndNodeDefinition` | 7 |
| `questLogicalHubNodeDefinition` | 5 |
| `questLogicalXorNodeDefinition` | 6 |
| `questMappinManagerNodeDefinition` | 2 |
| `questMiscAICommandNode` | 2 |
| `questMiscAICommandNode[questCombatNodeParams_RestrictMovementToArea]` | 2 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 1 |
| `questOutputNodeDefinition` | 10 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterAttack_ConditionType,questCharacterCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHealth_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 5 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 6 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 4 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryVisited_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questUICondition,questUIElement_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questObjectCondition,questScan_ConditionType]` | 5 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 7 |
| `questPauseConditionNodeDefinition[questSensesCondition,questVision_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 12 |
| `questPhaseNodeDefinition` | 9 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 6 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 5 |
| `questStartNodeDefinition` | 1 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 2 |
| `questVehicleNodeDefinition[questMoveOnSpline_NodeType]` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 6 |
| `questVoicesetManagerNodeDefinition[questChangeVoicesetState_NodeType,questChangeVoicesetState_NodeTypeParams]` | 2 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 4 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |
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
| `4db18aaae4b08d077f4e` | 4 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_22\ma_wat_nid_22_phase.questphase` / h238 / 12 -> 39 -> 40 |
| `bff957bf33a10413a685` | 4 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_22\ma_wat_nid_22_phase.questphase` / h426 / 9 -> 10 -> 14 |
| `05059c37b6a13b873408` | 3 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_22\ma_wat_nid_22_phase.questphase` / h426 / 39 -> 11 -> 12 |
| `226d1512a93078df2116` | 3 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_22\ma_wat_nid_22_phase.questphase` / h426 / 8 -> 39 -> 9 |
| `7e7dbbc930b3717fd790` | 3 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_22\ma_wat_nid_22_phase.questphase` / h0 / 32 -> 13 -> 14 |
| `131b32350d75ba8b8bfe` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_22\scenes\ma_wat_nid_22_clues.scene` / scene / 280 -> 262 -> 268 |
| `18be198845c90c6bb3c8` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_22\ma_wat_nid_22_phase.questphase` / h238 / 5 -> 12 -> 39 |
| `1e139970da956d2e7c3f` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_22\ma_wat_nid_22_phase.questphase` / h426 / 8 -> 39 -> 18 |
| `323f35ef4340038f6a80` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_22\ma_wat_nid_22_phase.questphase` / h1314 / 9 -> 4 -> 10 |
| `570676cffa83a3c52c8e` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_22\ma_wat_nid_22_phase.questphase` / h0 / 0 -> 129 -> 99 |
| `820115462266a8cd87c8` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_22\ma_wat_nid_22_phase.questphase` / h1314 / 4 -> 10 -> 7 |
| `844410923a2a8884163b` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_22\ma_wat_nid_22_phase.questphase` / h1314 / 9 -> 10 -> 7 |
| `9af8a87f20a910659fa8` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_22\ma_wat_nid_22_phase.questphase` / h0 / 152 -> 117 -> 118 |
| `ac5b347c9518873a2790` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_22\scenes\ma_wat_nid_22_clues.scene` / scene / 262 -> 268 -> 266 |
| `b1ff4db30ad594857e2e` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_22\ma_wat_nid_22_phase.questphase` / h1314 / 5 -> 12 -> 13 |
| `bbf9efd740881cf31a37` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_22\scenes\ma_wat_nid_22_clues.scene` / scene / 277 -> 280 -> 262 |
| `cb342d602e28e6bfccc1` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_22\ma_wat_nid_22_phase.questphase` / h0 / 147 -> 179 -> 209 |
| `d6b7c21f5d2d0ab76fc6` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_22\scenes\ma_wat_nid_22_clues.scene` / scene / 120 -> 121 -> 38 |
| `e5742f9794e6583c67cb` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_22\scenes\ma_wat_nid_22_clues.scene` / scene / 125 -> 120 -> 121 |
| `f1cab9108d90f7f5b3df` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_22\ma_wat_nid_22_phase.questphase` / h0 / 149 -> 160 -> 151 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
