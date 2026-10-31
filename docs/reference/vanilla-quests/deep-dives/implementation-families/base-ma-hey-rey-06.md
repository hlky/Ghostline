# base-ma-hey-rey-06

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_06\communities\ma_hey_rey_06_after.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_06\communities\ma_hey_rey_06_enemies.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_06\communities\ma_hey_rey_06_victims_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_06\ma_hey_rey_06.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_06\ma_hey_rey_06.quest` | content candidate | 2 / 0 | base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_06\ma_hey_rey_06_phase.questphase; base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_06\scenes\ma_hey_rey_06_chicken_test.scene; base\quest\holocalls\holocall_initializers.questphase |
| `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_06\ma_hey_rey_06_phase.questphase` | content candidate | 2 / 0 | base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_06\scenes\ma_hey_rey_06_holocall_brief.scene |
| `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_06\scenes\ma_hey_rey_06_chicken_test.scene` | test/debug | 0 / 4 |  |
| `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_06\scenes\ma_hey_rey_06_holocall_brief.scene` | content candidate | 0 / 15 |  |

## Journal paths observed in these resources

- `contacts/ncpd_dispatcher/outposts/ma_hey_rey_06`
- `points_of_interest/minor_activities/ma_hey_rey_06`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questPhoneMuted_ConditionType,questSystemCondition]` | 1 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 4 |
| `questCutControlNodeDefinition` | 7 |
| `questDeletionMarkerNodeDefinition` | 13 |
| `questEventManagerNodeDefinition` | 3 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 12 |
| `questInputNodeDefinition` | 3 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 1 |
| `questLogicalAndNodeDefinition` | 1 |
| `questLogicalHubNodeDefinition` | 1 |
| `questMiscAICommandNode` | 7 |
| `questMiscAICommandNode[questCombatNodeParams_RestrictMovementToArea]` | 1 |
| `questOutputNodeDefinition` | 3 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 8 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 8 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questContentCondition,questContentLock_ConditionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 6 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 2 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 5 |
| `questPhaseNodeDefinition` | 3 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 2 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 19 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 2 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 2 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 6 |
| `scnChoiceNode[scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnEndNode[scnNodeId]` | 4 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 1 |
| `scnStartNode[scnNodeId]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `95b7458b3ffd83fd4357` | 7 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_06\ma_hey_rey_06_phase.questphase` / h0 / 2 -> 3 -> 4 |
| `3206172ff6953fc6881f` | 6 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_06\ma_hey_rey_06_phase.questphase` / h0 / 103 -> 160 -> 159 |
| `3ba86c71a70bfb0620a5` | 6 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_06\ma_hey_rey_06_phase.questphase` / h0 / 101 -> 102 -> 103 |
| `484f47d527266442c50f` | 6 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_06\ma_hey_rey_06_phase.questphase` / h0 / 107 -> 106 -> 101 |
| `5466f936f30ed8ee354a` | 6 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_06\ma_hey_rey_06_phase.questphase` / h0 / 106 -> 101 -> 102 |
| `7373ce40c215f78fb39e` | 6 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_06\ma_hey_rey_06_phase.questphase` / h0 / 101 -> 102 -> 105 |
| `7d700b658871d4fd6b45` | 6 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_06\ma_hey_rey_06_phase.questphase` / h0 / 68 -> 107 -> 106 |
| `8edf5416ccd8dce9db72` | 6 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_06\ma_hey_rey_06_phase.questphase` / h0 / 106 -> 105 -> 103 |
| `c7b377e841e63de88f17` | 6 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_06\ma_hey_rey_06_phase.questphase` / h0 / 107 -> 106 -> 105 |
| `cadb89472ec2335d17b1` | 6 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_06\ma_hey_rey_06_phase.questphase` / h0 / 102 -> 105 -> 103 |
| `bfe95df47bd1ca67330f` | 4 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_06\ma_hey_rey_06_phase.questphase` / h179 / 33 -> 34 -> 38 |
| `e5742f9794e6583c67cb` | 3 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_06\scenes\ma_hey_rey_06_holocall_brief.scene` / scene / 64 -> 256 -> 258 |
| `02a5265bcccfc8e3cf77` | 2 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_06\ma_hey_rey_06_phase.questphase` / h179 / 31 -> 30 -> 32 |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_06\ma_hey_rey_06_phase.questphase` / h0 / 54 -> 151 -> 70 |
| `9e5e28ecb38ea2a53a15` | 2 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_06\scenes\ma_hey_rey_06_holocall_brief.scene` / scene / 254 -> 64 -> 58 |
| `d6b7c21f5d2d0ab76fc6` | 2 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_06\scenes\ma_hey_rey_06_holocall_brief.scene` / scene / 256 -> 258 -> 260 |
| `0672ae8d2fae884916ec` | 1 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_06\ma_hey_rey_06_phase.questphase` / h179 / 30 -> 32 -> 39 |
| `07708100a0a35824ab4a` | 1 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_06\ma_hey_rey_06_phase.questphase` / h0 / 183 -> 88 -> 184 |
| `0cc371503245695a1ef7` | 1 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_06\ma_hey_rey_06_phase.questphase` / h0 / 68 -> 72 -> 75 |
| `101b60945ddf6f25f378` | 1 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_06\scenes\ma_hey_rey_06_holocall_brief.scene` / scene / 24 -> 63 -> 65 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
