# base-sts-wbr-jpn-03

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\community\sts_wbr_jpn_03_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\community\sts_wbr_jpn_03_com_enemies.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\phase\sts_wbr_jpn_03_bugfixing.questphase` | repair | 5 / 0 |  |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\phase\sts_wbr_jpn_03_combat.questphase` | content candidate | 4 / 0 | base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\scenes\sts_wbr_jpn_03_scene.scene |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\phase\sts_wbr_jpn_03_phase.questphase` | content candidate | 1 / 0 | base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\phase\sts_wbr_jpn_03_combat.questphase; base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\phase\sts_wbr_jpn_03_streetstory.questphase |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\phase\sts_wbr_jpn_03_streetstory.questphase` | content candidate | 4 / 0 | base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\scenes\sts_wbr_jpn_03_holocall_debrief.scene; base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\scenes\sts_wbr_jpn_03_holocall_prebrief.scene |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\scenes\sts_wbr_jpn_03_holocall_debrief.scene` | content candidate | 0 / 25 |  |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\scenes\sts_wbr_jpn_03_holocall_prebrief.scene` | content candidate | 0 / 22 |  |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\scenes\sts_wbr_jpn_03_scene.scene` | content candidate | 0 / 16 |  |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\sts_wbr_jpn_03.quest` | content candidate | 2 / 0 | base\open_world\community\westbrook\japan_town\phases\wbr_jpn_phase.questphase; base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\phase\sts_wbr_jpn_03_phase.questphase; base\open_world\vendors\westbrook\japantown\wbr_jpn_junk_03\wbr_jpn_junk_03.scene; base\quest\holocalls\holocall_initializers.questphase |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\sts_wbr_jpn_03_gamedef.gamedef` | content candidate | 0 / 0 |  |

## Journal paths observed in these resources

- `contacts/wakako_okada/sts_wbr_jpn_03/jpn_03_additional_reward`
- `contacts/wakako_okada/sts_wbr_jpn_03/jpn_03_brief`
- `contacts/wakako_okada/sts_wbr_jpn_03/sts_wbr_jpn_03_debrief_non_stealth`
- `contacts/wakako_okada/sts_wbr_jpn_03/sts_wbr_jpn_03_debrief_stealth`
- `points_of_interest/street_stories/sts_wbr_jpn_03`
- `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_03`
- `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_03/sts_wbr_jpn_03/escape_shrone`
- `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_03/sts_wbr_jpn_03/find_way_in`
- `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_03/sts_wbr_jpn_03/get_special_reward`
- `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_03/sts_wbr_jpn_03/plant_bug_in_honden`
- `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_03/sts_wbr_jpn_03/stealth`
- `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_03/sts_wbr_jpn_03_brief`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questTriggerCondition,questVarComparison_ConditionType]` | 3 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 7 |
| `questConditionNodeDefinition[questPhoneMuted_ConditionType,questSystemCondition]` | 3 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 1 |
| `questDeletionMarkerNodeDefinition` | 14 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 29 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 34 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 6 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 1 |
| `questInputNodeDefinition` | 15 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 30 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 2 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 20 |
| `questMiscAICommandNode` | 4 |
| `questMovePuppetNodeDefinition[questMoveToParams,questUniversalRef]` | 1 |
| `questOutputNodeDefinition` | 13 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questCharacterStatusEffect_CondtionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterWorkspot_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 3 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 10 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questSceneCondition,questSceneNode_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 10 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 9 |
| `questPhaseNodeDefinition` | 16 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 2 |
| `questSceneNodeDefinition[scnWorldMarker]` | 6 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 9 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawnSet_NodeType]` | 1 |
| `questStartNodeDefinition` | 1 |
| `questUIManagerNodeDefinition[questProgressBar_NodeType]` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 6 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |
| `scnCutControlNode[scnNodeId]` | 2 |
| `scnDeletionMarkerNode[scnNodeId]` | 2 |
| `scnEndNode[scnNodeId]` | 9 |
| `scnHubNode[scnNodeId]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 8 |
| `scnStartNode[scnNodeId]` | 7 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `9380dda43f90ecd62efb` | 15 | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\phase\sts_wbr_jpn_03_bugfixing.questphase` / h17 / 7 -> 8 -> 9 |
| `8cd3b647ae3f592ad947` | 5 | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\scenes\sts_wbr_jpn_03_scene.scene` / scene / 149 -> 151 -> 150 |
| `2cb6a780f07f49d4270b` | 4 | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\phase\sts_wbr_jpn_03_bugfixing.questphase` / h17 / 9 -> 10 -> 1 |
| `bbf9efd740881cf31a37` | 4 | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\scenes\sts_wbr_jpn_03_holocall_debrief.scene` / scene / 249 -> 271 -> 252 |
| `d6b7c21f5d2d0ab76fc6` | 4 | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\scenes\sts_wbr_jpn_03_holocall_debrief.scene` / scene / 283 -> 281 -> 285 |
| `101b60945ddf6f25f378` | 3 | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\scenes\sts_wbr_jpn_03_holocall_debrief.scene` / scene / 27 -> 74 -> 76 |
| `138cff49923a75e07348` | 3 | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\phase\sts_wbr_jpn_03_streetstory.questphase` / h158 / 4 -> 17 -> 18 |
| `e5742f9794e6583c67cb` | 3 | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\scenes\sts_wbr_jpn_03_holocall_debrief.scene` / scene / 76 -> 71 -> 72 |
| `eaf5aab427d50e5598b6` | 3 | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\phase\sts_wbr_jpn_03_bugfixing.questphase` / h17 / 0 -> 12 -> 11 |
| `eb7dde8c18f400aec601` | 3 | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\phase\sts_wbr_jpn_03_bugfixing.questphase` / h85 / 3 -> 4 -> 5 |
| `03255fb9f4732b1c3d91` | 2 | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\phase\sts_wbr_jpn_03_streetstory.questphase` / h158 / 65 -> 101 -> 68 |
| `065b4a8c9cf295eae1bb` | 2 | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\phase\sts_wbr_jpn_03_combat.questphase` / h43 / 24 -> 17 -> 48 |
| `07708100a0a35824ab4a` | 2 | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\phase\sts_wbr_jpn_03_streetstory.questphase` / h158 / 102 -> 65 -> 101 |
| `10d2bed67733d8456950` | 2 | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\scenes\sts_wbr_jpn_03_holocall_debrief.scene` / scene / 271 -> 70 -> 73 |
| `129f2cf1d416edbd0fd1` | 2 | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\scenes\sts_wbr_jpn_03_holocall_debrief.scene` / scene / 249 -> 271 -> 70 |
| `131b32350d75ba8b8bfe` | 2 | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\scenes\sts_wbr_jpn_03_holocall_prebrief.scene` / scene / 269 -> 273 -> 279 |
| `1666d7526b9bab74f2e2` | 2 | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\phase\sts_wbr_jpn_03_streetstory.questphase` / h158 / 4 -> 15 -> 20 |
| `1d39f43a6624a803cd8a` | 2 | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\phase\sts_wbr_jpn_03_streetstory.questphase` / h158 / 102 -> 101 -> 68 |
| `1d933adb5a617880c93e` | 2 | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\scenes\sts_wbr_jpn_03_holocall_debrief.scene` / scene / 74 -> 76 -> 71 |
| `2beeeaa3b4da5300c035` | 2 | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\scenes\sts_wbr_jpn_03_holocall_debrief.scene` / scene / 1 -> 279 -> 75 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
