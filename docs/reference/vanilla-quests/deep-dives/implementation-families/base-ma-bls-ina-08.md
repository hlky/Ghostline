# base-ma-bls-ina-08

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\community\ma_bls_ina_se1_08_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08.quest` | content candidate | 1 / 0 | base\quest\additional_game_elements.questphase |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08_phase.questphase` | content candidate | 10 / 0 | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\scenes\ma_bls_ina_se1_08_holocall.scene |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\scenes\ma_bls_ina_se1_08_holocall.scene` | content candidate | 0 / 22 |  |

## Journal paths observed in these resources

- `contacts/regina_jones/ma_bls_ina_se1_08/00_msg_intro`
- `contacts/regina_jones/ma_bls_ina_se1_08/00_msg_start`
- `contacts/regina_jones/ma_bls_ina_se1_08/01_ch_info`
- `contacts/regina_jones/ma_bls_ina_se1_08/01_ch_info/01_ch_info`
- `contacts/regina_jones/ma_bls_ina_se1_08/01_ch_info_lethal`
- `contacts/regina_jones/ma_bls_ina_se1_08/01_ch_info_lethal/01_ch_info_lethal`
- `contacts/regina_jones/ma_bls_ina_se1_08/02_msg_regina`
- `contacts/regina_jones/ma_bls_ina_se1_08/02_msg_regina_lethal`
- `onscreens/emails/quests/minor_activities/badlands/se1/ma_bls_ina_se1_08/onscreens/ma_bls_ina_se1_08_onscreen_01`
- `onscreens/emails/quests/minor_activities/badlands/se1/ma_bls_ina_se1_08/onscreens/ma_bls_ina_se1_08_onscreen_02`
- `points_of_interest/minor_quests/ma_bls_ina_se1_08`
- `quests/minor_quest/ma_bls_ina_se1_08`
- `quests/minor_quest/ma_bls_ina_se1_08/description`
- `quests/minor_quest/ma_bls_ina_se1_08/ma_bls_ina_se1_08/check_shard`
- `quests/minor_quest/ma_bls_ina_se1_08/ma_bls_ina_se1_08/check_woman_shard`
- `quests/minor_quest/ma_bls_ina_se1_08/ma_bls_ina_se1_08/clues`
- `quests/minor_quest/ma_bls_ina_se1_08/ma_bls_ina_se1_08/clues/arena`
- `quests/minor_quest/ma_bls_ina_se1_08/ma_bls_ina_se1_08/clues/arena_large`
- `quests/minor_quest/ma_bls_ina_se1_08/ma_bls_ina_se1_08/clues/cp`
- `quests/minor_quest/ma_bls_ina_se1_08/ma_bls_ina_se1_08/kill`
- `quests/minor_quest/ma_bls_ina_se1_08/ma_bls_ina_se1_08/search`
- `quests/minor_quest/ma_bls_ina_se1_08/ma_bls_ina_se1_08/send_info`
- `quests/minor_quest/ma_bls_ina_se1_08/ma_bls_ina_se1_08/send_info/contact`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioMixNodeType]` | 9 |
| `questAudioNodeDefinition[questRadioAnnouncementNodeType,questRadioStationAnnouncementEventStruct]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_Kill,questCharacterManagerCombat_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questCombatNodeDefinition` | 2 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 1 |
| `questCombatNodeDefinition[questCombatNodeParams_ShootAt]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 2 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition,questPhoneMuted_ConditionType,questSystemCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition]` | 2 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryVisited_ConditionType]` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCutControlNodeDefinition` | 4 |
| `questDeletionMarkerNodeDefinition` | 5 |
| `questEntityManagerNodeDefinition[questEntityManagerToggleComponent_NodeType,questEntityManagerToggleComponent_NodeTypeParams]` | 1 |
| `questEventManagerNodeDefinition` | 5 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 20 |
| `questInputNodeDefinition` | 10 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 6 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 2 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 22 |
| `questJournalNodeDefinition[questJournalTrackQuest_NodeType]` | 1 |
| `questLogicalAndNodeDefinition` | 3 |
| `questLogicalHubNodeDefinition` | 7 |
| `questLogicalXorNodeDefinition` | 5 |
| `questMappinManagerNodeDefinition` | 4 |
| `questMiscAICommandNode` | 1 |
| `questMovePuppetNodeDefinition` | 1 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 1 |
| `questOutputNodeDefinition` | 11 |
| `questPauseConditionNodeDefinition[questCharacterAttack_ConditionType,questCharacterCondition]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PuppetSubType]` | 3 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 2 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 7 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 4 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryVisited_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questUICondition,questUIElement_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questObjectCondition,questScan_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 18 |
| `questPauseConditionNodeDefinition[questSensesCondition,questVision_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 12 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleSpeed_ConditionType]` | 1 |
| `questPhaseNodeDefinition` | 10 |
| `questPuppetAIManagerNodeDefinition[questPuppetAIManagerNodeDefinitionEntry]` | 3 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 2 |
| `questSceneNodeDefinition[scnWorldMarker]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 1 |
| `questStartNodeDefinition` | 1 |
| `questVehicleNodeDefinition[questRequestVehicleCameraPerspective_NodeType]` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 3 |
| `questVehicleNodeDefinition[questToggleForceBrake_NodeType]` | 1 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 3 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 1 |
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
| `29c7ac4763cf8bc766bd` | 8 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08_phase.questphase` / h1214 / 7 -> 3 -> 4 |
| `8c7beb1704f04b204046` | 8 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08_phase.questphase` / h1214 / 4 -> 5 -> 6 |
| `ee4b344701c562aa4943` | 8 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08_phase.questphase` / h1214 / 3 -> 4 -> 5 |
| `754bb5014790dc669c0d` | 4 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08_phase.questphase` / h0 / 99 -> 180 -> 98 |
| `815c1815268f980fb912` | 4 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08_phase.questphase` / h1214 / 0 -> 8 -> 7 |
| `a909c836470d2b0e7fbc` | 3 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08_phase.questphase` / h1214 / 0 -> 11 -> 1 |
| `bb5f35239f984c46ce98` | 3 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08_phase.questphase` / h0 / 180 -> 176 -> 139 |
| `131b32350d75ba8b8bfe` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\scenes\ma_bls_ina_se1_08_holocall.scene` / scene / 428 -> 408 -> 414 |
| `17ac46a4b3857ae17048` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08_phase.questphase` / h332 / 134 -> 105 -> 34 |
| `1814642825aef5741f77` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08_phase.questphase` / h0 / 178 -> 98 -> 177 |
| `21a735d428abaea4a228` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08_phase.questphase` / h0 / 113 -> 114 -> 148 |
| `240148efc76953d1c5d4` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08_phase.questphase` / h0 / 123 -> 124 -> 125 |
| `3e6f03030764fcc75954` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08_phase.questphase` / h0 / 98 -> 100 -> 99 |
| `8bd54738c2c85f70192e` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08_phase.questphase` / h0 / 92 -> 93 -> 22 |
| `8dd3932a10644218e399` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08_phase.questphase` / h0 / 139 -> 141 -> 180 |
| `8f4812f7bbc76781ef9f` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08_phase.questphase` / h332 / 137 -> 134 -> 105 |
| `ac5b347c9518873a2790` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\scenes\ma_bls_ina_se1_08_holocall.scene` / scene / 408 -> 414 -> 412 |
| `b7636bafa84868e336b5` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08_phase.questphase` / h0 / 217 -> 216 -> 84 |
| `bbf9efd740881cf31a37` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\scenes\ma_bls_ina_se1_08_holocall.scene` / scene / 423 -> 428 -> 408 |
| `bf65d680c627d4bbfc35` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08_phase.questphase` / h0 / 99 -> 180 -> 177 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
