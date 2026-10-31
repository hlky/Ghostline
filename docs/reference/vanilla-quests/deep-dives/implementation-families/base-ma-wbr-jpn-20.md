# base-ma-wbr-jpn-20

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_20\community\ma_wbr_jpn_20_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_20\community\ma_wbr_jpn_outpost_capturers_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_20\ma_wbr_jpn_20.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_20\ma_wbr_jpn_20.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_20\ma_wbr_jpn_20_phase.questphase; base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_20\scenes\ma_wbr_jpn_20_chicken_test.scene |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_20\ma_wbr_jpn_20_phase.questphase` | content candidate | 5 / 0 | base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_20\scenes\ma_wbr_jpn_20_holocall_brief.scene |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_20\scenes\ma_wbr_jpn_20_chicken_test.scene` | test/debug | 0 / 5 |  |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_20\scenes\ma_wbr_jpn_20_holocall_brief.scene` | content candidate | 0 / 15 |  |

## Journal paths observed in these resources

- `contacts/ncpd_dispatcher/outposts/ma_wbr_jpn_20`
- `points_of_interest/minor_activities/ma_wbr_jpn_20`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questPhoneMuted_ConditionType,questSystemCondition]` | 1 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 8 |
| `questCutControlNodeDefinition` | 1 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questEventManagerNodeDefinition` | 14 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 13 |
| `questInputNodeDefinition` | 5 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 9 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 2 |
| `questLogicalHubNodeDefinition` | 3 |
| `questMiscAICommandNode` | 2 |
| `questOutputNodeDefinition` | 2 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questContentCondition,questContentLock_ConditionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 2 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 2 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 2 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneNode_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 4 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 2 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 20 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 3 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 2 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 5 |
| `scnChoiceNode[scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnEndNode[scnNodeId]` | 5 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 1 |
| `scnStartNode[scnNodeId]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `3a8defbc2d61eaa66a75` | 8 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_20\ma_wbr_jpn_20_phase.questphase` / h105 / 68 -> 4 -> 31 |
| `5b6dcb2d96f16a7e8e23` | 6 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_20\ma_wbr_jpn_20_phase.questphase` / h0 / 84 -> 115 -> 116 |
| `66e17bf07a534afe17b2` | 6 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_20\ma_wbr_jpn_20_phase.questphase` / h105 / 68 -> 4 -> 16 |
| `18940bb88414fed7fad4` | 4 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_20\ma_wbr_jpn_20_phase.questphase` / h0 / 10 -> 132 -> 133 |
| `e5742f9794e6583c67cb` | 3 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_20\scenes\ma_wbr_jpn_20_holocall_brief.scene` / scene / 65 -> 258 -> 256 |
| `1982decfa315c06233bf` | 2 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_20\ma_wbr_jpn_20_phase.questphase` / h500 / 23 -> 25 -> 26 |
| `99c738f69bc472a4bcbf` | 2 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_20\ma_wbr_jpn_20_phase.questphase` / h0 / 26 -> 96 -> 97 |
| `9e5e28ecb38ea2a53a15` | 2 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_20\scenes\ma_wbr_jpn_20_holocall_brief.scene` / scene / 254 -> 65 -> 59 |
| `d6b7c21f5d2d0ab76fc6` | 2 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_20\scenes\ma_wbr_jpn_20_holocall_brief.scene` / scene / 258 -> 256 -> 260 |
| `ff33b6658cd80637b360` | 2 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_20\ma_wbr_jpn_20_phase.questphase` / h500 / 25 -> 26 -> 27 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_20\ma_wbr_jpn_20_phase.questphase` / h0 / 29 -> 138 -> 137 |
| `0b81e5206696faa510d4` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_20\ma_wbr_jpn_20_phase.questphase` / h105 / 11 -> 15 -> 25 |
| `0f660f7484731cdb671e` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_20\ma_wbr_jpn_20_phase.questphase` / h0 / 138 -> 26 -> 96 |
| `101b60945ddf6f25f378` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_20\scenes\ma_wbr_jpn_20_holocall_brief.scene` / scene / 29 -> 64 -> 66 |
| `12b102391853a0e26cba` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_20\ma_wbr_jpn_20_phase.questphase` / h105 / 6 -> 11 -> 15 |
| `14d7f1f2f390b216461a` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_20\ma_wbr_jpn_20_phase.questphase` / h0 / 111 -> 145 -> 112 |
| `1520ebe4ea0bf9451321` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_20\ma_wbr_jpn_20_phase.questphase` / h0 / 30 -> 129 -> 111 |
| `18be198845c90c6bb3c8` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_20\ma_wbr_jpn_20_phase.questphase` / h105 / 68 -> 4 -> 6 |
| `1b89a735937e920c2637` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_20\ma_wbr_jpn_20_phase.questphase` / h105 / 24 -> 28 -> 65 |
| `1d933adb5a617880c93e` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_20\scenes\ma_wbr_jpn_20_holocall_brief.scene` / scene / 64 -> 66 -> 61 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
