# base-sts-wat-kab-102

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_102\community\sts_wat_kab_102_crowd_community.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_102\community\sts_wat_kab_102_guards.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_102\community\sts_wat_kab_102_prestate_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_102\phases\sts_wat_kab_102.questphase` | content candidate | 1 / 0 | base\open_world\street_stories\watson\kabuki\sts_wat_kab_102\phases\sts_wat_kab_102_combat.questphase; base\open_world\street_stories\watson\kabuki\sts_wat_kab_102\phases\sts_wat_kab_102_openworld.questphase |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_102\phases\sts_wat_kab_102_after.questphase` | content candidate | 1 / 0 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_102\phases\sts_wat_kab_102_bugfixing.questphase` | repair | 2 / 0 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_102\phases\sts_wat_kab_102_combat.questphase` | content candidate | 3 / 0 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_102\phases\sts_wat_kab_102_openworld.questphase` | content candidate | 4 / 0 | base\open_world\street_stories\watson\kabuki\sts_wat_kab_102\scenes\sts_wat_kab_102_holocall_debrief.scene; base\open_world\street_stories\watson\kabuki\sts_wat_kab_102\scenes\sts_wat_kab_102_holocall_prebrief.scene |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_102\phases\sts_wat_kab_102_prestate_control.questphase` | content candidate | 1 / 0 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_102\scenes\sts_wat_kab_102_holocall_debrief.scene` | content candidate | 0 / 28 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_102\scenes\sts_wat_kab_102_holocall_prebrief.scene` | content candidate | 0 / 22 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_102\scenes\wat_kab_102_car_interaction_001.scene` | content candidate | 0 / 3 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_102\sts_wat_kab_102.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_102\sts_wat_kab_102.quest` | content candidate | 1 / 0 | base\open_world\street_stories\watson\kabuki\sts_wat_kab_102\phases\sts_wat_kab_102.questphase |

## Journal paths observed in these resources

- `contacts/regina_jones/sts_wat_kab_102/brief`
- `contacts/regina_jones/sts_wat_kab_102/special_reward_info`
- `contacts/regina_jones/sts_wat_kab_102/sts_wat_kab_102_debrief_fail`
- `contacts/regina_jones/sts_wat_kab_102/sts_wat_kab_102_debrief_not_perfect`
- `contacts/regina_jones/sts_wat_kab_102/sts_wat_kab_102_debrief_perfect`
- `points_of_interest/street_stories/sts_wat_kab_102`
- `quests/street_stories/watson/kabuki/sts_wat_kab_102`
- `quests/street_stories/watson/kabuki/sts_wat_kab_102/brief`
- `quests/street_stories/watson/kabuki/sts_wat_kab_102/sts_wat_kab_102/find_cargo_with_car`
- `quests/street_stories/watson/kabuki/sts_wat_kab_102/sts_wat_kab_102/get_special_reward`
- `quests/street_stories/watson/kabuki/sts_wat_kab_102/sts_wat_kab_102/get_to_docks`
- `quests/street_stories/watson/kabuki/sts_wat_kab_102/sts_wat_kab_102/leave_docks`
- `quests/street_stories/watson/kabuki/sts_wat_kab_102/sts_wat_kab_102/plant_tracker`
- `quests/street_stories/watson/kabuki/sts_wat_kab_102/sts_wat_kab_102/stealth`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 9 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 1 |
| `questConditionNodeDefinition[questPhoneMuted_ConditionType,questSystemCondition]` | 4 |
| `questCutControlNodeDefinition` | 1 |
| `questDeletionMarkerNodeDefinition` | 19 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 18 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 36 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 7 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 1 |
| `questInputNodeDefinition` | 13 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 4 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 3 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 22 |
| `questLogicalAndNodeDefinition` | 2 |
| `questLogicalHubNodeDefinition` | 2 |
| `questLogicalXorNodeDefinition` | 3 |
| `questMiscAICommandNode` | 5 |
| `questOutputNodeDefinition` | 11 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHealth_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questCharacterStatusEffect_CondtionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 2 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 8 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questSceneCondition,questSceneNode_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questObjectCondition,questScan_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 15 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 8 |
| `questPhaseNodeDefinition` | 8 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 2 |
| `questSceneNodeDefinition[scnWorldMarker]` | 4 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 4 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 7 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 3 |
| `scnChoiceNode[scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnCutControlNode[scnNodeId]` | 2 |
| `scnDeletionMarkerNode[scnNodeId]` | 2 |
| `scnEndNode[scnNodeId]` | 5 |
| `scnHubNode[scnNodeId]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 4 |
| `scnStartNode[scnNodeId]` | 3 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `101b60945ddf6f25f378` | 4 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_102\scenes\sts_wat_kab_102_holocall_debrief.scene` / scene / 29 -> 129 -> 130 |
| `bbf9efd740881cf31a37` | 4 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_102\scenes\sts_wat_kab_102_holocall_debrief.scene` / scene / 264 -> 267 -> 249 |
| `d6b7c21f5d2d0ab76fc6` | 4 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_102\scenes\sts_wat_kab_102_holocall_debrief.scene` / scene / 127 -> 128 -> 2 |
| `e5742f9794e6583c67cb` | 4 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_102\scenes\sts_wat_kab_102_holocall_debrief.scene` / scene / 130 -> 127 -> 128 |
| `07708100a0a35824ab4a` | 3 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_102\phases\sts_wat_kab_102_openworld.questphase` / h98 / 142 -> 81 -> 141 |
| `260a0eeffeaa533b5c20` | 3 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_102\phases\sts_wat_kab_102_openworld.questphase` / h98 / 112 -> 120 -> 132 |
| `2dd74f90a9c2399ed896` | 3 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_102\phases\sts_wat_kab_102_openworld.questphase` / h98 / 119 -> 138 -> 139 |
| `4365cb473b16f3e76999` | 3 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_102\phases\sts_wat_kab_102_openworld.questphase` / h98 / 142 -> 81 -> 110 |
| `48bba046d6d269fec85b` | 3 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_102\phases\sts_wat_kab_102_openworld.questphase` / h98 / 96 -> 112 -> 120 |
| `5b20c9cc6552e0be5bdc` | 3 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_102\phases\sts_wat_kab_102_openworld.questphase` / h98 / 119 -> 138 -> 87 |
| `6ea58e757157e77562cf` | 3 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_102\phases\sts_wat_kab_102_openworld.questphase` / h98 / 120 -> 132 -> 119 |
| `711e2813e6718693dc4e` | 3 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_102\phases\sts_wat_kab_102_openworld.questphase` / h98 / 132 -> 119 -> 138 |
| `94042083b3898e089d98` | 3 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_102\scenes\sts_wat_kab_102_holocall_debrief.scene` / scene / 118 -> 33 -> 29 |
| `a53561b4c002bc02b58a` | 3 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_102\phases\sts_wat_kab_102_openworld.questphase` / h98 / 4 -> 5 -> 6 |
| `ad08ea1a65ff6f3e8622` | 3 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_102\scenes\sts_wat_kab_102_holocall_debrief.scene` / scene / 117 -> 118 -> 33 |
| `b769ade732d21ee6cf4f` | 3 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_102\phases\sts_wat_kab_102_openworld.questphase` / h98 / 142 -> 81 -> 109 |
| `ef7fc81dcc0c722d269f` | 3 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_102\scenes\sts_wat_kab_102_holocall_debrief.scene` / scene / 33 -> 29 -> 129 |
| `03255fb9f4732b1c3d91` | 2 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_102\phases\sts_wat_kab_102_openworld.questphase` / h98 / 81 -> 141 -> 79 |
| `10d2bed67733d8456950` | 2 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_102\scenes\sts_wat_kab_102_holocall_debrief.scene` / scene / 267 -> 117 -> 118 |
| `129f2cf1d416edbd0fd1` | 2 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_102\scenes\sts_wat_kab_102_holocall_debrief.scene` / scene / 264 -> 267 -> 117 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
