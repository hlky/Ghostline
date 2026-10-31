# base-sts-std-arr-03

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_03\community\sts_std_arr_03_cars.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_03\community\sts_std_arr_03_combat_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_03\community\sts_std_arr_03_non_combat_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_03\community\sts_std_arr_03_reinforcements.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_03\community\sts_std_arr_03_scaffolding.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_03\phases\sts_std_arr_03.questphase` | content candidate | 1 / 0 | base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_03\phases\sts_std_arr_03_gameplay_phase.questphase; base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_03\phases\sts_std_arr_03_openworld_phase.questphase |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_03\phases\sts_std_arr_03_gameplay_phase.questphase` | content candidate | 17 / 0 | base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_03\scenes\sts_std_arr_03_entrance_booth.scene; base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_03\scenes\sts_std_arr_03_phone_main_entrance.scene; base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_03\scenes\sts_std_arr_03_workers_talk.scene |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_03\phases\sts_std_arr_03_openworld_phase.questphase` | content candidate | 7 / 0 | base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_03\scenes\sts_std_arr_03_holocall_debriefs.scene; base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_03\scenes\sts_std_arr_03_holocall_prebrief.scene |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_03\scenes\sts_std_arr_03_entrance_booth.scene` | content candidate | 0 / 4 |  |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_03\scenes\sts_std_arr_03_holocall_debriefs.scene` | content candidate | 0 / 25 |  |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_03\scenes\sts_std_arr_03_holocall_prebrief.scene` | content candidate | 0 / 22 |  |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_03\scenes\sts_std_arr_03_phone_main_entrance.scene` | content candidate | 0 / 4 |  |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_03\scenes\sts_std_arr_03_workers_talk.scene` | content candidate | 0 / 5 |  |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_03\sts_std_arr_03.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_03\sts_std_arr_03.quest` | content candidate | 1 / 0 | base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_03\phases\sts_std_arr_03.questphase; base\quest\holocalls\holocall_initializers.questphase |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_03\sts_std_arr_03_test_world.gamedef` | content candidate | 0 / 0 |  |

## Journal paths observed in these resources

- `contacts/muamar_el_capitan_reyes/sts_std_arr_03/sts_std_arr_03_brief`
- `contacts/muamar_el_capitan_reyes/sts_std_arr_03/sts_std_arr_03_data_received`
- `contacts/muamar_el_capitan_reyes/sts_std_arr_03/sts_std_arr_03_holocall_debrief_perfect`
- `points_of_interest/street_stories/sts_std_arr_03`
- `quests/street_stories/santo_domingo/arroyo/sts_std_arr_03`
- `quests/street_stories/santo_domingo/arroyo/sts_std_arr_03/brifing`
- `quests/street_stories/santo_domingo/arroyo/sts_std_arr_03/sts_std_arr_03/find_disk`
- `quests/street_stories/santo_domingo/arroyo/sts_std_arr_03/sts_std_arr_03/get_data`
- `quests/street_stories/santo_domingo/arroyo/sts_std_arr_03/sts_std_arr_03/get_ground`
- `quests/street_stories/santo_domingo/arroyo/sts_std_arr_03/sts_std_arr_03/get_inside`
- `quests/street_stories/santo_domingo/arroyo/sts_std_arr_03/sts_std_arr_03/leave_area`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetReactionPreset,questReactionPresetRecordSelector]` | 4 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 2 |
| `questConditionNodeDefinition[questPhoneMuted_ConditionType,questSystemCondition]` | 2 |
| `questDeletionMarkerNodeDefinition` | 7 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 6 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 24 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 4 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 1 |
| `questInputNodeDefinition` | 25 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 7 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 3 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 13 |
| `questLogicalAndNodeDefinition` | 7 |
| `questLogicalHubNodeDefinition` | 2 |
| `questLogicalXorNodeDefinition` | 4 |
| `questMiscAICommandNode` | 10 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 3 |
| `questOutputNodeDefinition` | 14 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 16 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questCharacterStatusEffect_CondtionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 14 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 6 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 8 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneInterrupt_ConditionType,scnCheckSpeakerDistractedInterruptCondition]` | 3 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneNode_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 15 |
| `questPhaseNodeDefinition` | 26 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneNodeDefinition[scnToggleInterruption_InterruptionOperation,scnWorldMarker]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 4 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 9 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 20 |
| `questStartNodeDefinition` | 1 |
| `questUIManagerNodeDefinition[questProgressBar_NodeType]` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 5 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 4 |
| `scnCutControlNode[scnNodeId]` | 2 |
| `scnDeletionMarkerNode[scnNodeId]` | 2 |
| `scnEndNode[scnNodeId]` | 8 |
| `scnHubNode[scnNodeId]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 5 |
| `scnStartNode[scnNodeId]` | 7 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `79ff30ab7464b071eda5` | 18 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_03\phases\sts_std_arr_03_openworld_phase.questphase` / h616 / 39 -> 40 -> 41 |
| `3535ee3b356c051e5fe9` | 6 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_03\phases\sts_std_arr_03_gameplay_phase.questphase` / h126 / 0 -> 3 -> 4 |
| `ea186520ba952298d781` | 6 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_03\phases\sts_std_arr_03_openworld_phase.questphase` / h788 / 41 -> 46 -> 27 |
| `6f633a1a8a493edf4436` | 5 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_03\phases\sts_std_arr_03_gameplay_phase.questphase` / h153 / 0 -> 3 -> 10 |
| `23a66f192f777a4c74f7` | 4 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_03\phases\sts_std_arr_03_gameplay_phase.questphase` / h126 / 3 -> 4 -> 1 |
| `bbf9efd740881cf31a37` | 4 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_03\scenes\sts_std_arr_03_holocall_debriefs.scene` / scene / 270 -> 259 -> 249 |
| `d6b7c21f5d2d0ab76fc6` | 4 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_03\scenes\sts_std_arr_03_holocall_debriefs.scene` / scene / 163 -> 164 -> 2 |
| `138cff49923a75e07348` | 3 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_03\phases\sts_std_arr_03_openworld_phase.questphase` / h12 / 13 -> 12 -> 14 |
| `2e362801d31d08a7d108` | 3 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_03\scenes\sts_std_arr_03_holocall_debriefs.scene` / scene / 279 -> 161 -> 270 |
| `3b70bb506b872cadfa43` | 3 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_03\scenes\sts_std_arr_03_entrance_booth.scene` / scene / 1 -> 10 -> 2 |
| `4e9253a72e6b0134b8dd` | 3 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_03\phases\sts_std_arr_03_openworld_phase.questphase` / h12 / 19 -> 20 -> 3 |
| `559744591d4f911a3931` | 3 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_03\phases\sts_std_arr_03_openworld_phase.questphase` / h974 / 0 -> 3 -> 2 |
| `8cd3b647ae3f592ad947` | 3 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_03\scenes\sts_std_arr_03_entrance_booth.scene` / scene / 1 -> 4 -> 2 |
| `dceacff78dfb78406240` | 3 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_03\phases\sts_std_arr_03_openworld_phase.questphase` / h788 / 41 -> 46 -> 21 |
| `e5742f9794e6583c67cb` | 3 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_03\scenes\sts_std_arr_03_holocall_debriefs.scene` / scene / 168 -> 163 -> 164 |
| `101b60945ddf6f25f378` | 2 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_03\scenes\sts_std_arr_03_holocall_debriefs.scene` / scene / 18 -> 166 -> 168 |
| `10d2bed67733d8456950` | 2 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_03\scenes\sts_std_arr_03_holocall_debriefs.scene` / scene / 259 -> 162 -> 165 |
| `129f2cf1d416edbd0fd1` | 2 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_03\scenes\sts_std_arr_03_holocall_debriefs.scene` / scene / 270 -> 259 -> 162 |
| `131b32350d75ba8b8bfe` | 2 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_03\scenes\sts_std_arr_03_holocall_prebrief.scene` / scene / 270 -> 274 -> 279 |
| `1437ef8be826c28f8233` | 2 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_03\phases\sts_std_arr_03_gameplay_phase.questphase` / h35 / 7 -> 8 -> 11 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
