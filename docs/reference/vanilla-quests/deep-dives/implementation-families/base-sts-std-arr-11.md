# base-sts-std-arr-11

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\community\sts_std_arr_011_flathead.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\community\sts_std_arr_11_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\community\sts_std_arr_11_reinforcement_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\community\sts_std_arr_11_tenant_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\phases\sts_std_arr_11_gameplay.questphase` | content candidate | 15 / 0 | base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\scenes\sts_std_arr_11_scene.scene |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\phases\sts_std_arr_11_openworld.questphase` | content candidate | 5 / 0 | base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\scenes\sts_std_arr_11_holocall_debrief.scene; base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\scenes\sts_std_arr_11_holocall_prebiref.scene |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\phases\sts_std_arr_11_phase.questphase` | content candidate | 1 / 0 | base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\phases\sts_std_arr_11_gameplay.questphase; base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\phases\sts_std_arr_11_openworld.questphase |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\scenes\sts_std_arr_11_holocall_debrief.scene` | content candidate | 0 / 25 |  |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\scenes\sts_std_arr_11_holocall_prebiref.scene` | content candidate | 0 / 22 |  |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\scenes\sts_std_arr_11_scene.scene` | content candidate | 0 / 3 |  |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\sts_std_arr_11_gamedef.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\sts_std_arr_11_gamedef_test.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\sts_std_arr_11_quest.quest` | content candidate | 1 / 0 | base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\phases\sts_std_arr_11_phase.questphase; base\quest\holocalls\holocall_initializers.questphase |

## Journal paths observed in these resources

- `contacts/muamar_el_capitan_reyes/sts_std_arr_11/brief`
- `contacts/muamar_el_capitan_reyes/sts_std_arr_11/sts_std_arr_11_debrief_not_perfect`
- `contacts/muamar_el_capitan_reyes/sts_std_arr_11/sts_std_arr_11_debrief_perfect`
- `points_of_interest/street_stories/sts_std_arr_11`
- `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11`
- `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/brief`
- `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/delete`
- `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/delete/computer_001`
- `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/eliminate_lucius`
- `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/get_inside`
- `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/get_inside_megabuilding`
- `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/get_inside_megabuilding/elevator`
- `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/get_out`
- `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/get_out/lab`
- `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/get_out/megabuilding`
- `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/get_to_the_drop_point`
- `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11/sts_std_arr_11/get_to_the_drop_point/elevator`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_ModifyHealth,questCharacterManagerCombat_NodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetReactionPreset,questReactionPresetRecordSelector]` | 2 |
| `questCheckpointNodeDefinition` | 4 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 6 |
| `questCombatNodeDefinition[questCombatNodeParams_UseCover]` | 3 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 4 |
| `questConditionNodeDefinition[questPhoneMuted_ConditionType,questSystemCondition]` | 3 |
| `questCutControlNodeDefinition` | 1 |
| `questDeletionMarkerNodeDefinition` | 10 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 8 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 32 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 7 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 1 |
| `questInputNodeDefinition` | 21 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 8 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 20 |
| `questMappinManagerNodeDefinition` | 10 |
| `questMiscAICommandNode` | 7 |
| `questOutputNodeDefinition` | 11 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questCharacterStatusEffect_CondtionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionFunctionParameter,questDevice_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 4 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 6 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 11 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneNode_ConditionType]` | 4 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 17 |
| `questPhaseNodeDefinition` | 17 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 5 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 2 |
| `questSceneNodeDefinition[scnWorldMarker]` | 4 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 6 |
| `questStartNodeDefinition` | 1 |
| `questUIManagerNodeDefinition[questProgressBar_NodeType]` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 7 |
| `questVisionModesManagerNodeDefinition[questForceModule_NodeType,questForceVMModule_NodeTypeParams]` | 1 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 13 |
| `scnCutControlNode[scnNodeId]` | 2 |
| `scnDeletionMarkerNode[scnNodeId]` | 2 |
| `scnEndNode[scnNodeId]` | 5 |
| `scnHubNode[scnNodeId]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnInterruptManagerNode[scnNodeId,scnToggleInterruption_InterruptionOperation]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 4 |
| `scnStartNode[scnNodeId]` | 3 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `bbf9efd740881cf31a37` | 4 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\scenes\sts_std_arr_11_holocall_debrief.scene` / scene / 263 -> 266 -> 269 |
| `d6b7c21f5d2d0ab76fc6` | 4 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\scenes\sts_std_arr_11_holocall_debrief.scene` / scene / 297 -> 295 -> 299 |
| `e5742f9794e6583c67cb` | 4 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\scenes\sts_std_arr_11_holocall_debrief.scene` / scene / 75 -> 297 -> 295 |
| `07708100a0a35824ab4a` | 3 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\phases\sts_std_arr_11_openworld.questphase` / h12 / 186 -> 152 -> 100 |
| `101b60945ddf6f25f378` | 3 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\scenes\sts_std_arr_11_holocall_debrief.scene` / scene / 28 -> 250 -> 70 |
| `4365cb473b16f3e76999` | 3 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\phases\sts_std_arr_11_openworld.questphase` / h12 / 186 -> 152 -> 163 |
| `4e9253a72e6b0134b8dd` | 3 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\phases\sts_std_arr_11_openworld.questphase` / h12 / 4 -> 104 -> 138 |
| `55cf1403fc66b8ebf602` | 3 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\phases\sts_std_arr_11_gameplay.questphase` / h357 / 17 -> 16 -> 18 |
| `6d673ec176c9c336e22f` | 3 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\phases\sts_std_arr_11_gameplay.questphase` / h357 / 17 -> 16 -> 19 |
| `81aad11c4a0a4b595895` | 3 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\phases\sts_std_arr_11_gameplay.questphase` / h357 / 8 -> 25 -> 7 |
| `9303706e2045d54f58b5` | 3 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\phases\sts_std_arr_11_openworld.questphase` / h12 / 47 -> 142 -> 145 |
| `b769ade732d21ee6cf4f` | 3 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\phases\sts_std_arr_11_openworld.questphase` / h12 / 186 -> 152 -> 162 |
| `051e569302308d155ee9` | 2 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\phases\sts_std_arr_11_openworld.questphase` / h12 / 7 -> 78 -> 79 |
| `129f2cf1d416edbd0fd1` | 2 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\scenes\sts_std_arr_11_holocall_debrief.scene` / scene / 263 -> 266 -> 74 |
| `131b32350d75ba8b8bfe` | 2 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\scenes\sts_std_arr_11_holocall_prebiref.scene` / scene / 270 -> 273 -> 279 |
| `18be198845c90c6bb3c8` | 2 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\phases\sts_std_arr_11_openworld.questphase` / h881 / 34 -> 35 -> 13 |
| `1d933adb5a617880c93e` | 2 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\scenes\sts_std_arr_11_holocall_debrief.scene` / scene / 250 -> 70 -> 68 |
| `25346aef8b8629a80cf8` | 2 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\phases\sts_std_arr_11_openworld.questphase` / h12 / 57 -> 174 -> 176 |
| `260a0eeffeaa533b5c20` | 2 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\phases\sts_std_arr_11_openworld.questphase` / h12 / 164 -> 168 -> 184 |
| `2beeeaa3b4da5300c035` | 2 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\scenes\sts_std_arr_11_holocall_debrief.scene` / scene / 21 -> 293 -> 75 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
