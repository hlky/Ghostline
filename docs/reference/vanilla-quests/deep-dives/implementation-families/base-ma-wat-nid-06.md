# base-ma-wat-nid-06

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_06\community\ma_wat_nid_06_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_06\ma_wat_nid_06.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_06\ma_wat_nid_06.quest` | content candidate | 2 / 0 | base\open_world\minor_activities\watson\northside\ma_wat_nid_06\ma_wat_nid_06_phase.questphase |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_06\ma_wat_nid_06_phase.questphase` | content candidate | 1 / 0 | base\open_world\minor_activities\watson\northside\ma_wat_nid_06\scenes\ma_wat_nid_06_holocall_brief.scene |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_06\scenes\ma_wat_nid_06_holocall_brief.scene` | content candidate | 0 / 15 |  |

## Journal paths observed in these resources

- `contacts/ncpd_dispatcher/outposts/ma_wat_nid_06`
- `onscreens/emails/quests/minor_activities/watson/norhside_industrial_district/ma_wat_nid_06/onscreens/ma_wat_nid_06_finger`
- `points_of_interest/minor_activities/ma_wat_nid_06`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questPhoneMuted_ConditionType,questSystemCondition]` | 1 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 3 |
| `questCutControlNodeDefinition` | 1 |
| `questDeletionMarkerNodeDefinition` | 5 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 5 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 15 |
| `questInputNodeDefinition` | 2 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 1 |
| `questLogicalAndNodeDefinition` | 1 |
| `questLogicalXorNodeDefinition` | 1 |
| `questMiscAICommandNode` | 6 |
| `questOutputNodeDefinition` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questContentCondition,questContentLock_ConditionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneNode_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 5 |
| `questPhaseNodeDefinition` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 1 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 1 |
| `questStartNodeDefinition` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 4 |
| `scnEndNode[scnNodeId]` | 2 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 1 |
| `scnStartNode[scnNodeId]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `0267b0e79efe88bdd513` | 5 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_06\ma_wat_nid_06_phase.questphase` / h0 / 69 -> 3 -> 5 |
| `85521418a2a3f3a27ee5` | 3 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_06\ma_wat_nid_06_phase.questphase` / h0 / 0 -> 113 -> 15 |
| `e5742f9794e6583c67cb` | 3 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_06\scenes\ma_wat_nid_06_holocall_brief.scene` / scene / 254 -> 258 -> 256 |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_06\ma_wat_nid_06_phase.questphase` / h0 / 30 -> 97 -> 75 |
| `579affdb9dc50dc1a027` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_06\ma_wat_nid_06_phase.questphase` / h0 / 69 -> 3 -> 30 |
| `5870e2fba5607932758d` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_06\ma_wat_nid_06_phase.questphase` / h0 / 3 -> 30 -> 39 |
| `9e5e28ecb38ea2a53a15` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_06\scenes\ma_wat_nid_06_holocall_brief.scene` / scene / 64 -> 254 -> 58 |
| `d6b7c21f5d2d0ab76fc6` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_06\scenes\ma_wat_nid_06_holocall_brief.scene` / scene / 258 -> 256 -> 260 |
| `d8c910d5272dfbd8cb9c` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_06\ma_wat_nid_06_phase.questphase` / h0 / 69 -> 3 -> 104 |
| `05059c37b6a13b873408` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_06\ma_wat_nid_06_phase.questphase` / h0 / 103 -> 69 -> 3 |
| `06e3382349ceff89de6f` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_06\ma_wat_nid_06_phase.questphase` / h0 / 91 -> 9 -> 77 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_06\ma_wat_nid_06_phase.questphase` / h0 / 120 -> 117 -> 116 |
| `0c8f031f372a34b54a46` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_06\ma_wat_nid_06_phase.questphase` / h0 / 110 -> 73 -> 111 |
| `101b60945ddf6f25f378` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_06\scenes\ma_wat_nid_06_holocall_brief.scene` / scene / 26 -> 63 -> 65 |
| `1398ec279d5314c176fb` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_06\ma_wat_nid_06_phase.questphase` / h0 / 113 -> 15 -> 20 |
| `14d7f1f2f390b216461a` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_06\ma_wat_nid_06_phase.questphase` / h0 / 87 -> 114 -> 88 |
| `18202b344e835623a4d8` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_06\ma_wat_nid_06.quest` / h0 / 3 -> 4 -> 0 |
| `1d933adb5a617880c93e` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_06\scenes\ma_wat_nid_06_holocall_brief.scene` / scene / 63 -> 65 -> 60 |
| `226d1512a93078df2116` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_06\ma_wat_nid_06_phase.questphase` / h0 / 1 -> 103 -> 69 |
| `243842ad9db2994d6abc` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_06\ma_wat_nid_06_phase.questphase` / h0 / 116 -> 92 -> 79 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
