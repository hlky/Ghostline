# base-sts-std-rcr-05

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\communities\sts_std_rcr_05.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\communities\sts_std_rcr_05_johnny.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\phases\sts_std_rcr_05.questphase` | content candidate | 1 / 0 | base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\phases\sts_std_rcr_05_gameplay.questphase; base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\phases\sts_std_rcr_05_openworld.questphase |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\phases\sts_std_rcr_05_bugfixing.questphase` | repair | 3 / 0 |  |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\phases\sts_std_rcr_05_gameplay.questphase` | content candidate | 5 / 0 | base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\sts_std_rcr_05_cyberpsycho.scene |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\phases\sts_std_rcr_05_openworld.questphase` | content candidate | 8 / 0 | base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\sts_std_rcr_05_clues.scene; base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\sts_std_rcr_05_holocall_debriefs.scene; base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\sts_std_rcr_05_holocall_prebrief.scene |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\sts_std_rcr_05_clues.scene` | content candidate | 0 / 89 |  |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\sts_std_rcr_05_cyberpsycho.scene` | content candidate | 0 / 46 |  |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\sts_std_rcr_05_holocall_debriefs.scene` | content candidate | 0 / 23 |  |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\sts_std_rcr_05_holocall_prebrief.scene` | content candidate | 0 / 22 |  |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\sts_std_rcr_05.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\sts_std_rcr_05.quest` | content candidate | 1 / 0 | base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\phases\sts_std_rcr_05.questphase; base\quest\holocalls\holocall_initializers.questphase |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\sts_std_rcr_05_nc.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\sts_std_rcr_05_test.gamedef` | content candidate | 0 / 0 |  |

## Journal paths observed in these resources

- `contacts/muamar_el_capitan_reyes/sts_std_rcr_05/brief`
- `contacts/muamar_el_capitan_reyes/sts_std_rcr_05/sts_std_arr_05_debrief`
- `points_of_interest/street_stories/sts_std_rcr_05`
- `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05`
- `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/briefing`
- `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/deliver`
- `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/find_way_to_open_safe`
- `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/go_to_house`
- `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/investigate`
- `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/investigate_house`
- `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/open_safe`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_Kill,questCharacterManagerCombat_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 9 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 3 |
| `questConditionNodeDefinition[questPhoneMuted_ConditionType,questSystemCondition]` | 2 |
| `questCutControlNodeDefinition` | 1 |
| `questDeletionMarkerNodeDefinition` | 7 |
| `questEndNodeDefinition` | 1 |
| `questEntityManagerNodeDefinition[questEntityManagerToggleComponent_NodeType,questEntityManagerToggleComponent_NodeTypeParams]` | 1 |
| `questEventManagerNodeDefinition` | 12 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 47 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 4 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 1 |
| `questInputNodeDefinition` | 17 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 10 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questItemManagerNodeDefinition[questSetItemTags_NodeType,questSetItemTags_NodeTypeParams,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 19 |
| `questLogicalAndNodeDefinition` | 2 |
| `questLogicalHubNodeDefinition` | 2 |
| `questLogicalXorNodeDefinition` | 3 |
| `questMiscAICommandNode` | 1 |
| `questOutputNodeDefinition` | 10 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questCharacterStatusEffect_CondtionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 11 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 6 |
| `questPauseConditionNodeDefinition[questObjectCondition,questScan_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 15 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneNode_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 15 |
| `questPhaseNodeDefinition` | 17 |
| `questRandomizerNodeDefinition` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneNodeDefinition[scnToggleInterruption_InterruptionOperation,scnWorldMarker]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 9 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 1 |
| `questStartNodeDefinition` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 14 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 2 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 6 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 5 |
| `scnChoiceNode[scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAttachToGameObjectParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 5 |
| `scnCutControlNode[scnNodeId]` | 2 |
| `scnDeletionMarkerNode[scnNodeId]` | 2 |
| `scnEndNode[scnNodeId]` | 13 |
| `scnHubNode[scnNodeId]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnRandomizerNode[scnNodeId]` | 7 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 27 |
| `scnStartNode[scnNodeId]` | 35 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `0c313b98f243e3372c3f` | 7 | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\sts_std_rcr_05_clues.scene` / scene / 93 -> 10 -> 57 |
| `3af95a0b36868c686aaa` | 7 | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\sts_std_rcr_05_cyberpsycho.scene` / scene / 403 -> 404 -> 406 |
| `4fcad87865f924474a76` | 7 | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\sts_std_rcr_05_cyberpsycho.scene` / scene / 403 -> 404 -> 405 |
| `12c5b59865f45697f18f` | 5 | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\sts_std_rcr_05_clues.scene` / scene / 89 -> 299 -> 301 |
| `1a3e365fa34d855352fe` | 5 | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\sts_std_rcr_05_clues.scene` / scene / 318 -> 105 -> 17 |
| `c1a16a62b98663759211` | 5 | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\sts_std_rcr_05_clues.scene` / scene / 299 -> 301 -> 93 |
| `20ed149604d1c2e68d57` | 4 | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\sts_std_rcr_05_clues.scene` / scene / 57 -> 60 -> 289 |
| `65b19b442f66ff9107ec` | 4 | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\phases\sts_std_rcr_05_bugfixing.questphase` / h12 / 9 -> 10 -> 11 |
| `9e6d24d44bb591bccb53` | 4 | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\sts_std_rcr_05_clues.scene` / scene / 150 -> 45 -> 66 |
| `ac1f6a8c9746094bd626` | 4 | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\phases\sts_std_rcr_05_openworld.questphase` / h128 / 4 -> 57 -> 5 |
| `bbf9efd740881cf31a37` | 4 | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\sts_std_rcr_05_holocall_debriefs.scene` / scene / 249 -> 272 -> 252 |
| `d0feae257f5e5216f8f9` | 4 | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\sts_std_rcr_05_clues.scene` / scene / 30 -> 45 -> 66 |
| `d6b7c21f5d2d0ab76fc6` | 4 | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\sts_std_rcr_05_holocall_debriefs.scene` / scene / 283 -> 281 -> 285 |
| `e5742f9794e6583c67cb` | 4 | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\sts_std_rcr_05_holocall_debriefs.scene` / scene / 66 -> 283 -> 281 |
| `f802ad66d4ceea2d0aff` | 3 | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\phases\sts_std_rcr_05_gameplay.questphase` / h215 / 0 -> 5 -> 6 |
| `07708100a0a35824ab4a` | 2 | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\phases\sts_std_rcr_05_openworld.questphase` / h128 / 89 -> 79 -> 78 |
| `101b60945ddf6f25f378` | 2 | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\sts_std_rcr_05_holocall_debriefs.scene` / scene / 27 -> 65 -> 67 |
| `10d2bed67733d8456950` | 2 | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\sts_std_rcr_05_holocall_debriefs.scene` / scene / 272 -> 61 -> 64 |
| `129f2cf1d416edbd0fd1` | 2 | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\sts_std_rcr_05_holocall_debriefs.scene` / scene / 249 -> 272 -> 61 |
| `131b32350d75ba8b8bfe` | 2 | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\sts_std_rcr_05_holocall_prebrief.scene` / scene / 270 -> 273 -> 279 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
