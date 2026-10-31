# base-sts-std-arr-10

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_10\community\sts_std_arr_10_car.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_10\community\sts_std_arr_10_community.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_10\community\sts_std_arr_10_workers_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_10\phases\sts_std_arr_10_bugfixing.questphase` | repair | 3 / 0 |  |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_10\phases\sts_std_arr_10_gameplay.questphase` | content candidate | 24 / 0 | base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_10\scenes\sts_std_arr_10_chats.scene; base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_10\scenes\sts_std_arr_10_enemy_005.scene |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_10\phases\sts_std_arr_10_open_world.questphase` | content candidate | 4 / 0 | base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_10\scenes\sts_std_arr_10_holocall_debriefs.scene; base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_10\scenes\sts_std_arr_10_holocall_prebrief.scene |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_10\phases\sts_std_arr_10_phase.questphase` | content candidate | 1 / 0 | base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_10\phases\sts_std_arr_10_gameplay.questphase; base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_10\phases\sts_std_arr_10_open_world.questphase |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_10\scenes\sts_std_arr_10_chats.scene` | content candidate | 0 / 10 |  |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_10\scenes\sts_std_arr_10_enemy_005.scene` | content candidate | 0 / 4 |  |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_10\scenes\sts_std_arr_10_holocall_debriefs.scene` | content candidate | 0 / 23 |  |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_10\scenes\sts_std_arr_10_holocall_prebrief.scene` | content candidate | 0 / 22 |  |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_10\sts_std_arr_10_gamedef.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_10\sts_std_arr_10_quest.quest` | content candidate | 1 / 0 | base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_10\phases\sts_std_arr_10_phase.questphase; base\quest\holocalls\holocall_initializers.questphase |

## Journal paths observed in these resources

- `contacts/muamar_el_capitan_reyes/sts_std_arr_10/arr_10_send_stolen_data`
- `contacts/muamar_el_capitan_reyes/sts_std_arr_10/brief`
- `contacts/muamar_el_capitan_reyes/sts_std_arr_10/send_data_sms_arr_10`
- `contacts/muamar_el_capitan_reyes/sts_std_arr_10/sts_std_arr_10_debrief`
- `points_of_interest/street_stories/sts_std_arr_10`
- `quests/street_stories/santo_domingo/arroyo/sts_std_arr_10`
- `quests/street_stories/santo_domingo/arroyo/sts_std_arr_10/brief`
- `quests/street_stories/santo_domingo/arroyo/sts_std_arr_10/sts_std_arr_10/get_in`
- `quests/street_stories/santo_domingo/arroyo/sts_std_arr_10/sts_std_arr_10/get_inside_factory_ground`
- `quests/street_stories/santo_domingo/arroyo/sts_std_arr_10/sts_std_arr_10/leave`
- `quests/street_stories/santo_domingo/arroyo/sts_std_arr_10/sts_std_arr_10/recover_data`
- `quests/street_stories/santo_domingo/arroyo/sts_std_arr_10/sts_std_arr_10/second_floor`
- `quests/street_stories/santo_domingo/arroyo/sts_std_arr_10/sts_std_arr_10/server_room`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 6 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 3 |
| `questConditionNodeDefinition[questPhoneMuted_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questCutControlNodeDefinition` | 1 |
| `questDeletionMarkerNodeDefinition` | 15 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 10 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 34 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 4 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 1 |
| `questInputNodeDefinition` | 32 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_ActionProperty,questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 1 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 33 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 4 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 19 |
| `questLogicalAndNodeDefinition` | 5 |
| `questLogicalXorNodeDefinition` | 2 |
| `questMiscAICommandNode` | 10 |
| `questMiscAICommandNode[questCombatNodeParams_RestrictMovementToArea]` | 1 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef,questWithCompanionMoveOnSplineParams]` | 1 |
| `questOutputNodeDefinition` | 9 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 14 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questCharacterStatusEffect_CondtionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 15 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 10 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneInterrupt_ConditionType,scnCheckSpeakerDistractedInterruptCondition]` | 3 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneNode_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 15 |
| `questPhaseNodeDefinition` | 30 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 2 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 6 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 9 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 4 |
| `questStartNodeDefinition` | 1 |
| `questUIManagerNodeDefinition[questProgressBar_NodeType]` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 1 |
| `questVoicesetManagerNodeDefinition[questChangeVoicesetState_NodeType,questChangeVoicesetState_NodeTypeParams]` | 1 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 2 |
| `scnCutControlNode[scnNodeId]` | 2 |
| `scnDeletionMarkerNode[scnNodeId]` | 2 |
| `scnEndNode[scnNodeId]` | 7 |
| `scnHubNode[scnNodeId]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 5 |
| `scnStartNode[scnNodeId]` | 5 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `a7e15504419b8801f5cd` | 9 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_10\phases\sts_std_arr_10_open_world.questphase` / h12 / 62 -> 64 -> 19 |
| `3a8defbc2d61eaa66a75` | 7 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_10\phases\sts_std_arr_10_open_world.questphase` / h779 / 36 -> 81 -> 52 |
| `da44faaa63ffe9d69306` | 7 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_10\phases\sts_std_arr_10_open_world.questphase` / h779 / 81 -> 52 -> 28 |
| `138cff49923a75e07348` | 6 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_10\phases\sts_std_arr_10_open_world.questphase` / h260 / 32 -> 31 -> 33 |
| `3535ee3b356c051e5fe9` | 6 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_10\phases\sts_std_arr_10_gameplay.questphase` / h109 / 0 -> 2 -> 3 |
| `4e9253a72e6b0134b8dd` | 4 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_10\phases\sts_std_arr_10_open_world.questphase` / h260 / 46 -> 47 -> 87 |
| `a53561b4c002bc02b58a` | 4 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_10\phases\sts_std_arr_10_open_world.questphase` / h260 / 30 -> 32 -> 31 |
| `bbf9efd740881cf31a37` | 4 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_10\scenes\sts_std_arr_10_holocall_debriefs.scene` / scene / 270 -> 261 -> 249 |
| `d6b7c21f5d2d0ab76fc6` | 4 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_10\scenes\sts_std_arr_10_holocall_debriefs.scene` / scene / 99 -> 100 -> 96 |
| `e5742f9794e6583c67cb` | 4 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_10\scenes\sts_std_arr_10_holocall_debriefs.scene` / scene / 103 -> 281 -> 283 |
| `1a3d0ec08c9c011c8d4e` | 3 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_10\phases\sts_std_arr_10_open_world.questphase` / h779 / 42 -> 51 -> 93 |
| `27dfce7ed75e337ef6f2` | 3 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_10\phases\sts_std_arr_10_open_world.questphase` / h12 / 64 -> 37 -> 22 |
| `3b70bb506b872cadfa43` | 3 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_10\scenes\sts_std_arr_10_chats.scene` / scene / 1 -> 57 -> 2 |
| `46bcc0d67487a3d77151` | 3 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_10\phases\sts_std_arr_10_open_world.questphase` / h779 / 64 -> 65 -> 42 |
| `61e233f151e81d37ca6d` | 3 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_10\phases\sts_std_arr_10_open_world.questphase` / h779 / 65 -> 42 -> 51 |
| `7ffce8649053214df83f` | 3 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_10\phases\sts_std_arr_10_gameplay.questphase` / h320 / 0 -> 2 -> 4 |
| `81cbdfd9be3a1544e45b` | 3 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_10\phases\sts_std_arr_10_open_world.questphase` / h779 / 46 -> 65 -> 42 |
| `f802ad66d4ceea2d0aff` | 3 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_10\phases\sts_std_arr_10_gameplay.questphase` / h600 / 0 -> 8 -> 10 |
| `101b60945ddf6f25f378` | 2 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_10\scenes\sts_std_arr_10_holocall_debriefs.scene` / scene / 43 -> 102 -> 104 |
| `10d2bed67733d8456950` | 2 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_10\scenes\sts_std_arr_10_holocall_debriefs.scene` / scene / 261 -> 98 -> 101 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
