# base-ma-std-arr-03

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\community\ma_std_arr_03_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\community\ma_std_arr_03_reinforcements.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\ma_std_arr_03.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\ma_std_arr_03.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\ma_std_arr_03_phase.questphase; base\quest\holocalls\holocall_initializers.questphase |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\ma_std_arr_03_phase.questphase` | content candidate | 3 / 0 | base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\scenes\ma_std_arr_03_holocall_brief.scene |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\phases\ma_std_arr_03_bugfixing.questphase` | repair | 4 / 0 | base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\scenes\ma_std_arr_03_holocall_brief.scene |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\scenes\ma_std_arr_03_holocall_brief.scene` | content candidate | 0 / 15 |  |

## Journal paths observed in these resources

- `contacts/ncpd_dispatcher/outposts/ma_std_arr_03`
- `points_of_interest/minor_activities/ma_std_arr_03`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 4 |
| `questCombatNodeDefinition` | 4 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 4 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 5 |
| `questConditionNodeDefinition[questPhoneMuted_ConditionType,questSystemCondition]` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 4 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 4 |
| `questCutControlNodeDefinition` | 2 |
| `questDeletionMarkerNodeDefinition` | 16 |
| `questEventManagerNodeDefinition` | 3 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 23 |
| `questInputNodeDefinition` | 8 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 2 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 4 |
| `questLogicalAndNodeDefinition` | 10 |
| `questLogicalHubNodeDefinition` | 4 |
| `questLogicalXorNodeDefinition` | 3 |
| `questMiscAICommandNode` | 20 |
| `questOutputNodeDefinition` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 9 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 12 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questContentCondition,questContentLock_ConditionType,questLogicalCondition,questTriggerCondition]` | 2 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 8 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 5 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 3 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 4 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneNode_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 8 |
| `questPhaseNodeDefinition` | 6 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 2 |
| `questSceneNodeDefinition[scnWorldMarker]` | 2 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 15 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 8 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]` | 4 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 20 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 2 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 10 |
| `scnEndNode[scnNodeId]` | 2 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 1 |
| `scnStartNode[scnNodeId]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `293a406889902f2a6921` | 10 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\ma_std_arr_03_phase.questphase` / h239 / 17 -> 20 -> 62 |
| `4c068ae78925bce2e854` | 10 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\ma_std_arr_03_phase.questphase` / h239 / 13 -> 15 -> 16 |
| `9f12a0f19618f810f032` | 10 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\ma_std_arr_03_phase.questphase` / h239 / 24 -> 45 -> 43 |
| `bb8f0c4585c266a3824e` | 10 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\ma_std_arr_03_phase.questphase` / h239 / 16 -> 20 -> 62 |
| `95b7458b3ffd83fd4357` | 8 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\ma_std_arr_03_phase.questphase` / h0 / 45 -> 58 -> 109 |
| `81b2abaa4525608463d1` | 6 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\ma_std_arr_03_phase.questphase` / h239 / 18 -> 20 -> 62 |
| `03debfbfcf1fc0991f59` | 4 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\ma_std_arr_03_phase.questphase` / h239 / 5 -> 13 -> 15 |
| `29a99096ea308b54f59e` | 4 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\ma_std_arr_03_phase.questphase` / h239 / 11 -> 12 -> 6 |
| `5949d96807ee7dfbe225` | 4 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\ma_std_arr_03_phase.questphase` / h239 / 6 -> 13 -> 15 |
| `6791cbbe6b26cff8e34a` | 4 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\ma_std_arr_03_phase.questphase` / h239 / 4 -> 11 -> 48 |
| `7576b3e62a6e7713a306` | 4 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\ma_std_arr_03_phase.questphase` / h239 / 29 -> 26 -> 30 |
| `83f969f185aa3330bfb1` | 4 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\ma_std_arr_03_phase.questphase` / h239 / 15 -> 16 -> 20 |
| `859c7585ed8be68e3151` | 4 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\ma_std_arr_03_phase.questphase` / h239 / 38 -> 36 -> 39 |
| `999952894b2b547e9107` | 4 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\ma_std_arr_03_phase.questphase` / h239 / 41 -> 22 -> 23 |
| `a31f7bd7cccaa866a166` | 4 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\ma_std_arr_03_phase.questphase` / h239 / 15 -> 17 -> 20 |
| `b0040516e4dddf5c906e` | 4 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\ma_std_arr_03_phase.questphase` / h239 / 17 -> 20 -> 9 |
| `c53959d739abdfe4a473` | 4 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\ma_std_arr_03_phase.questphase` / h239 / 16 -> 20 -> 9 |
| `c9170fb2e5c18a121162` | 4 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\ma_std_arr_03_phase.questphase` / h239 / 4 -> 11 -> 12 |
| `cd0897a21972132ec435` | 4 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\ma_std_arr_03_phase.questphase` / h239 / 11 -> 12 -> 5 |
| `e94253629713cb091a99` | 4 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\ma_std_arr_03_phase.questphase` / h239 / 29 -> 25 -> 30 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
