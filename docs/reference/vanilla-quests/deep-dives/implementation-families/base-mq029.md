# base-mq029

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\quest\bugfixing\minor_quests\mq029\mq029_cinematic_bugfixes.questphase` | repair | 2 / 0 |  |
| `base\quest\bugfixing\minor_quests\mq029\mq029_encounter_bugfixes.questphase` | repair | 2 / 0 |  |
| `base\quest\bugfixing\minor_quests\mq029\mq029_quest_bugfixes.questphase` | repair | 4 / 0 |  |
| `base\quest\minor_quests\mq029\communities\mq029_com_james.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq029\mq029_tourist.gamedef` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq029\mq029_tourist.quest` | content candidate | 4 / 0 | base\quest\minor_quests\mq029\mq029_tourist.questphase; base\quest\minor_quests\mq029\scenes\test\mq029_xx_debug.scene |
| `base\quest\minor_quests\mq029\mq029_tourist.questphase` | content candidate | 2 / 0 | base\quest\minor_quests\mq029\phases\mq029_garage.questphase; base\quest\minor_quests\mq029\phases\mq029_james.questphase; base\quest\minor_quests\mq029\phases\mq029_josie_corpse.questphase; base\quest\minor_quests\mq029\phases\mq029_setup.questphase; base\quest\minor_quests\mq029\phases\mq029_stolen_bike.questphase |
| `base\quest\minor_quests\mq029\phases\mq029_garage.questphase` | content candidate | 1 / 0 | base\quest\minor_quests\mq029\scenes\mq029_01a_garage.scene |
| `base\quest\minor_quests\mq029\phases\mq029_james.questphase` | content candidate | 1 / 0 | base\quest\minor_quests\mq029\scenes\mq029_01_james.scene |
| `base\quest\minor_quests\mq029\phases\mq029_josie_corpse.questphase` | content candidate | 2 / 0 | base\quest\minor_quests\mq029\scenes\mq029_01b_josie_body.scene |
| `base\quest\minor_quests\mq029\phases\mq029_setup.questphase` | content candidate | 1 / 0 |  |
| `base\quest\minor_quests\mq029\phases\mq029_stolen_bike.questphase` | content candidate | 2 / 0 |  |
| `base\quest\minor_quests\mq029\scenes\mq029_01_james.scene` | content candidate | 0 / 79 |  |
| `base\quest\minor_quests\mq029\scenes\mq029_01a_garage.scene` | content candidate | 0 / 19 |  |
| `base\quest\minor_quests\mq029\scenes\mq029_01b_josie_body.scene` | content candidate | 0 / 11 |  |
| `base\quest\minor_quests\mq029\scenes\test\mq029_xx_debug.scene` | test/debug | 0 / 16 |  |

## Journal paths observed in these resources

- `quests/main_quest/act_01/q101_01_firestorm`
- `quests/main_quest/prologue/q001_01_victor`
- `quests/main_quest/prologue/q001_02_dex`
- `quests/main_quest/prologue/q001_intro`
- `quests/main_quest/prologue/q003_maelstrom`
- `quests/main_quest/prologue/q003_stout`
- `quests/main_quest/prologue/q004_braindance`
- `quests/main_quest/prologue/q005_heist`
- `quests/minor_quest/mq029_tourist`
- `quests/minor_quest/mq029_tourist/mq029_tourist_new/mq029_confront_james`
- `quests/minor_quest/mq029_tourist/mq029_tourist_new/mq029_confront_james/mq029_james`
- `quests/minor_quest/mq029_tourist/mq029_tourist_new/mq029_find_bike`
- `quests/minor_quest/mq029_tourist/mq029_tourist_new/mq029_find_bike/mq029_bike_desc`
- `quests/minor_quest/mq029_tourist/mq029_tourist_new/mq029_find_garage`
- `quests/minor_quest/mq029_tourist/mq029_tourist_new/mq029_find_garage/find_garage`
- `quests/minor_quest/mq029_tourist/mq029_tourist_new/mq029_find_james`
- `quests/minor_quest/mq029_tourist/mq029_tourist_new/mq029_find_james/find_james_desc`
- `quests/minor_quest/mq029_tourist/mq029_tourist_new/mq029_find_josie_new`
- `quests/minor_quest/mq029_tourist/mq029_tourist_new/mq029_find_josie_new/mappin_area`
- `quests/minor_quest/mq029_tourist/mq029_tourist_new/mq029_find_josie_new/mq029_garage`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioMixNodeType]` | 2 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 2 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetReactionPreset,questReactionPresetRecordSelector]` | 2 |
| `questCheckpointNodeDefinition` | 4 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 4 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 18 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questCutControlNodeDefinition` | 1 |
| `questDeletionMarkerNodeDefinition` | 7 |
| `questEventManagerNodeDefinition` | 14 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 19 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 8 |
| `questInputNodeDefinition` | 20 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 5 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 13 |
| `questLogicalAndNodeDefinition` | 2 |
| `questLogicalHubNodeDefinition` | 2 |
| `questLogicalXorNodeDefinition` | 4 |
| `questMappinManagerNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 17 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 3 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 8 |
| `questPauseConditionNodeDefinition[questInputAction_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questNodeLoadingCondition]` | 1 |
| `questPauseConditionNodeDefinition[questObjectCondition,questScan_ConditionType]` | 9 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 2 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSectionNode_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 5 |
| `questPhaseNodeDefinition` | 14 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneManagerNodeDefinition[questSetTier_NodeType]` | 4 |
| `questSceneNodeDefinition[scnWorldMarker]` | 5 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 1 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 6 |
| `questTimeManagerNodeDefinition[questSetTime_NodeType]` | 1 |
| `questUIManagerNodeDefinition[questDisplayMessageBox_NodeType]` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 9 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 12 |
| `questVehicleNodeDefinition[questEnablePlayerVehicle_NodeType]` | 3 |
| `questVoicesetManagerNodeDefinition[questChangeVoicesetState_NodeType,questChangeVoicesetState_NodeTypeParams]` | 2 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 1 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 1 |
| `scnChoiceNode[questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 3 |
| `scnChoiceNode[scnChoiceNodeNsAttachToGameObjectParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 4 |
| `scnChoiceNode[scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 1 |
| `scnCutControlNode[scnNodeId]` | 2 |
| `scnDeletionMarkerNode[scnNodeId]` | 2 |
| `scnEndNode[scnNodeId]` | 14 |
| `scnHubNode[scnNodeId]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 19 |
| `scnStartNode[scnNodeId]` | 10 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `abbf46d00a7c0ae464b9` | 11 | `base\quest\bugfixing\minor_quests\mq029\mq029_quest_bugfixes.questphase` / h59 / 2 -> 3 -> 4 |
| `0564448edf0e7538168f` | 9 | `base\quest\minor_quests\mq029\phases\mq029_josie_corpse.questphase` / h46 / 4 -> 14 -> 17 |
| `194c96834df1b666d3d7` | 9 | `base\quest\minor_quests\mq029\phases\mq029_josie_corpse.questphase` / h46 / 6 -> 14 -> 17 |
| `94715a2859451160c268` | 9 | `base\quest\minor_quests\mq029\phases\mq029_josie_corpse.questphase` / h46 / 2 -> 14 -> 17 |
| `ffa42caa6bf1990e8e9c` | 9 | `base\quest\minor_quests\mq029\phases\mq029_josie_corpse.questphase` / h46 / 5 -> 14 -> 17 |
| `79a2f966cbd172f86eaa` | 4 | `base\quest\minor_quests\mq029\phases\mq029_stolen_bike.questphase` / h63 / 2 -> 3 -> 14 |
| `0109d4b38c5fe1325697` | 2 | `base\quest\minor_quests\mq029\scenes\mq029_01_james.scene` / scene / 174 -> 162 -> 196 |
| `06f2bacc7391706d2a72` | 2 | `base\quest\minor_quests\mq029\phases\mq029_stolen_bike.questphase` / h63 / 8 -> 13 -> 1 |
| `081b9dbe9528f984ddca` | 2 | `base\quest\minor_quests\mq029\scenes\mq029_01_james.scene` / scene / 11 -> 63 -> 69 |
| `0dd22b61b6238907b258` | 2 | `base\quest\minor_quests\mq029\phases\mq029_garage.questphase` / h0 / 55 -> 57 -> 59 |
| `0edb5530c623e3c0f1e6` | 2 | `base\quest\minor_quests\mq029\scenes\mq029_01_james.scene` / scene / 174 -> 162 -> 196 |
| `13c71f1e28d70e8f7a0f` | 2 | `base\quest\minor_quests\mq029\scenes\mq029_01_james.scene` / scene / 174 -> 164 -> 159 |
| `7634b00ab1f0486e332f` | 2 | `base\quest\minor_quests\mq029\scenes\mq029_01_james.scene` / scene / 174 -> 164 -> 159 |
| `78dc11b12cb662fc606c` | 2 | `base\quest\minor_quests\mq029\scenes\mq029_01_james.scene` / scene / 61 -> 174 -> 162 |
| `7ec231ce276c7278bb69` | 2 | `base\quest\minor_quests\mq029\scenes\mq029_01_james.scene` / scene / 11 -> 63 -> 230 |
| `8920e9f26b68bff49d8b` | 2 | `base\quest\minor_quests\mq029\scenes\mq029_01_james.scene` / scene / 57 -> 61 -> 88 |
| `8c44b341c66b9d795cde` | 2 | `base\quest\minor_quests\mq029\phases\mq029_stolen_bike.questphase` / h63 / 6 -> 8 -> 13 |
| `d7ddeb5e2c4bd5f2a5b0` | 2 | `base\quest\minor_quests\mq029\scenes\mq029_01_james.scene` / scene / 61 -> 174 -> 162 |
| `dbeb8824cf54dd13f915` | 2 | `base\quest\minor_quests\mq029\scenes\mq029_01_james.scene` / scene / 209 -> 208 -> 214 |
| `dd719f474c0091e3d3bd` | 2 | `base\quest\bugfixing\minor_quests\mq029\mq029_quest_bugfixes.questphase` / h59 / 0 -> 2 -> 3 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
