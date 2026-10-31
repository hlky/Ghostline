# base-sts-wat-lch-01

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_01\community\sts_wat_lch_01_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_01\phase\sts_wat_lch_01_combat.questphase` | content candidate | 4 / 0 | base\open_world\street_stories\watson\little_china\sts_wat_lch_01\scenes\sts_wat_lch_01_enemies.scene |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_01\phase\sts_wat_lch_01_openworld.questphase` | content candidate | 5 / 0 | base\open_world\street_stories\watson\little_china\sts_wat_lch_01\scenes\sts_wat_lch_01_holocall_debrief.scene; base\open_world\street_stories\watson\little_china\sts_wat_lch_01\scenes\sts_wat_lch_01_holocall_prebrief.scene |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_01\phase\sts_wat_lch_01_phase.questphase` | content candidate | 1 / 0 | base\open_world\street_stories\watson\little_china\sts_wat_lch_01\phase\sts_wat_lch_01_combat.questphase; base\open_world\street_stories\watson\little_china\sts_wat_lch_01\phase\sts_wat_lch_01_openworld.questphase |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_01\phase\sts_wat_lch_01_prestate_control.questphase` | content candidate | 1 / 0 |  |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_01\scenes\sts_wat_lch_01_enemies.scene` | content candidate | 0 / 25 |  |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_01\scenes\sts_wat_lch_01_holocall_debrief.scene` | content candidate | 0 / 23 |  |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_01\scenes\sts_wat_lch_01_holocall_prebrief.scene` | content candidate | 0 / 22 |  |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_01\sts_wat_lch_01.quest` | content candidate | 1 / 0 | base\open_world\street_stories\watson\little_china\sts_wat_lch_01\phase\sts_wat_lch_01_phase.questphase; base\quest\holocalls\holocall_initializers.questphase |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_01\sts_wat_lch_01_gamedef.gamedef` | content candidate | 0 / 0 |  |

## Journal paths observed in these resources

- `contacts/regina_jones/sts_wat_lch_01/brief`
- `contacts/regina_jones/sts_wat_lch_01/sts_wat_lch_01_debrief`
- `points_of_interest/street_stories/sts_wat_lch_01`
- `quests/street_stories/watson/little_china/sts_wat_lch_01`
- `quests/street_stories/watson/little_china/sts_wat_lch_01/brief`
- `quests/street_stories/watson/little_china/sts_wat_lch_01/sts_wat_lch_01/get_out`
- `quests/street_stories/watson/little_china/sts_wat_lch_01/sts_wat_lch_01/get_to_server_room`
- `quests/street_stories/watson/little_china/sts_wat_lch_01/sts_wat_lch_01/upload_software`
- `quests/street_stories/watson/little_china/sts_wat_lch_01/sts_wat_lch_01/upload_software/upload_software_mp`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 2 |
| `questConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 2 |
| `questConditionNodeDefinition[questPhoneMuted_ConditionType,questSystemCondition]` | 2 |
| `questCutControlNodeDefinition` | 1 |
| `questDeletionMarkerNodeDefinition` | 8 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 28 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 5 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 1 |
| `questInputNodeDefinition` | 11 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_ActionProperty,questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 1 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 4 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 2 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 8 |
| `questLogicalAndNodeDefinition` | 1 |
| `questLogicalXorNodeDefinition` | 1 |
| `questMappinManagerNodeDefinition` | 2 |
| `questMiscAICommandNode` | 2 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 1 |
| `questMovePuppetNodeDefinition[questMoveToParams,questUniversalRef]` | 3 |
| `questOutputNodeDefinition` | 11 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questLogicalCondition,questSystemCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterQuickHacked_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questCharacterStatusEffect_CondtionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterStatusEffect_CondtionType]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterWorkspot_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 3 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 7 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questObjectCondition,questScan_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 5 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneInterrupt_ConditionType,scnCheckAnyoneDistractedInterruptCondition]` | 1 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneInterrupt_ConditionType,scnCheckSpeakerDistractedInterruptCondition]` | 5 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneNode_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 9 |
| `questPhaseNodeDefinition` | 11 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 3 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 9 |
| `questStartNodeDefinition` | 1 |
| `questUIManagerNodeDefinition[questProgressBar_NodeType]` | 1 |
| `scnCutControlNode[scnNodeId]` | 2 |
| `scnDeletionMarkerNode[scnNodeId]` | 2 |
| `scnEndNode[scnNodeId]` | 10 |
| `scnHubNode[scnNodeId]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 8 |
| `scnStartNode[scnNodeId]` | 8 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `8cd3b647ae3f592ad947` | 5 | `base\open_world\street_stories\watson\little_china\sts_wat_lch_01\scenes\sts_wat_lch_01_enemies.scene` / scene / 62 -> 47 -> 63 |
| `3b70bb506b872cadfa43` | 4 | `base\open_world\street_stories\watson\little_china\sts_wat_lch_01\scenes\sts_wat_lch_01_enemies.scene` / scene / 72 -> 108 -> 73 |
| `bbf9efd740881cf31a37` | 4 | `base\open_world\street_stories\watson\little_china\sts_wat_lch_01\scenes\sts_wat_lch_01_holocall_debrief.scene` / scene / 249 -> 272 -> 252 |
| `d6b7c21f5d2d0ab76fc6` | 4 | `base\open_world\street_stories\watson\little_china\sts_wat_lch_01\scenes\sts_wat_lch_01_holocall_debrief.scene` / scene / 283 -> 281 -> 285 |
| `e5742f9794e6583c67cb` | 4 | `base\open_world\street_stories\watson\little_china\sts_wat_lch_01\scenes\sts_wat_lch_01_holocall_debrief.scene` / scene / 66 -> 283 -> 281 |
| `0e5f3402118a8d470b09` | 2 | `base\open_world\street_stories\watson\little_china\sts_wat_lch_01\phase\sts_wat_lch_01_combat.questphase` / h70 / 19 -> 13 -> 11 |
| `101b60945ddf6f25f378` | 2 | `base\open_world\street_stories\watson\little_china\sts_wat_lch_01\scenes\sts_wat_lch_01_holocall_debrief.scene` / scene / 24 -> 58 -> 59 |
| `10d2bed67733d8456950` | 2 | `base\open_world\street_stories\watson\little_china\sts_wat_lch_01\scenes\sts_wat_lch_01_holocall_debrief.scene` / scene / 272 -> 64 -> 65 |
| `129f2cf1d416edbd0fd1` | 2 | `base\open_world\street_stories\watson\little_china\sts_wat_lch_01\scenes\sts_wat_lch_01_holocall_debrief.scene` / scene / 249 -> 272 -> 64 |
| `131b32350d75ba8b8bfe` | 2 | `base\open_world\street_stories\watson\little_china\sts_wat_lch_01\scenes\sts_wat_lch_01_holocall_prebrief.scene` / scene / 270 -> 273 -> 279 |
| `138cff49923a75e07348` | 2 | `base\open_world\street_stories\watson\little_china\sts_wat_lch_01\phase\sts_wat_lch_01_openworld.questphase` / h75 / 12 -> 18 -> 19 |
| `1d933adb5a617880c93e` | 2 | `base\open_world\street_stories\watson\little_china\sts_wat_lch_01\scenes\sts_wat_lch_01_holocall_debrief.scene` / scene / 58 -> 59 -> 56 |
| `2251a3c44ea8a153bc79` | 2 | `base\open_world\street_stories\watson\little_china\sts_wat_lch_01\phase\sts_wat_lch_01_combat.questphase` / h12 / 0 -> 12 -> 9 |
| `26762f051e7728f090ca` | 2 | `base\open_world\street_stories\watson\little_china\sts_wat_lch_01\scenes\sts_wat_lch_01_holocall_debrief.scene` / scene / 64 -> 65 -> 24 |
| `2beeeaa3b4da5300c035` | 2 | `base\open_world\street_stories\watson\little_china\sts_wat_lch_01\scenes\sts_wat_lch_01_holocall_debrief.scene` / scene / 1 -> 279 -> 66 |
| `2e362801d31d08a7d108` | 2 | `base\open_world\street_stories\watson\little_china\sts_wat_lch_01\scenes\sts_wat_lch_01_holocall_debrief.scene` / scene / 66 -> 63 -> 249 |
| `3fe0ae98a8cf5496b004` | 2 | `base\open_world\street_stories\watson\little_china\sts_wat_lch_01\phase\sts_wat_lch_01_openworld.questphase` / h75 / 53 -> 55 -> 54 |
| `55e6bb9b78b34a0b16c1` | 2 | `base\open_world\street_stories\watson\little_china\sts_wat_lch_01\phase\sts_wat_lch_01_combat.questphase` / h70 / 32 -> 17 -> 29 |
| `67763c1be07ab727409e` | 2 | `base\open_world\street_stories\watson\little_china\sts_wat_lch_01\phase\sts_wat_lch_01_combat.questphase` / h70 / 17 -> 29 -> 19 |
| `69a2aad2f79abb156101` | 2 | `base\open_world\street_stories\watson\little_china\sts_wat_lch_01\scenes\sts_wat_lch_01_holocall_debrief.scene` / scene / 63 -> 249 -> 272 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
