# base-mws-wat-02

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\mini_world_stories\watson\mws_wat_02\mws_wat_02.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\watson\mws_wat_02\mws_wat_02.quest` | content candidate | 1 / 0 | base\open_world\mini_world_stories\watson\mws_wat_02\mws_wat_02.questphase |
| `base\open_world\mini_world_stories\watson\mws_wat_02\mws_wat_02.questphase` | content candidate | 3 / 0 | base\open_world\mini_world_stories\watson\mws_wat_02\scenes\mws_wat_02.scene |
| `base\open_world\mini_world_stories\watson\mws_wat_02\scenes\mws_wat_02.scene` | content candidate | 0 / 109 |  |

## Journal paths observed in these resources

- `ep1/quests/main_quest/q305_border_crossing/08_border_crossing/10_talk_to_johnny`
- `quests/main_quest/epilogues/q203_legend/penthouse/enter_delemain`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 11 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 3 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 22 |
| `questInputNodeDefinition` | 5 |
| `questItemManagerNodeDefinition[questAddRemoveItem_NodeType,questAddRemoveItem_NodeTypeParams,questUniversalRef]` | 2 |
| `questItemManagerNodeDefinition[questSetItemTags_NodeType,questSetItemTags_NodeTypeParams,questUniversalRef]` | 1 |
| `questLogicalHubNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 5 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 4 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 7 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 13 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 1 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 2 |
| `questSceneNodeDefinition[scnWorldMarker]` | 3 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 10 |
| `questStartNodeDefinition` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 4 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 4 |
| `questVisionModesManagerNodeDefinition[questEnableScanning_NodeType]` | 3 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 11 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 10 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 3 |
| `scnAndNode[scnNodeId]` | 1 |
| `scnChoiceNode[questFactsDBCondition,questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition,questVarComparison_ConditionType,scnChoiceNodeNsAttachToWorldParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 2 |
| `scnCutControlNode[scnNodeId]` | 3 |
| `scnHubNode[scnNodeId]` | 5 |
| `scnRandomizerNode[scnNodeId]` | 2 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 10 |
| `scnStartNode[scnNodeId]` | 4 |
| `scnXorNode[scnNodeId]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `0d920badc92f6f64a45f` | 3 | `base\open_world\mini_world_stories\watson\mws_wat_02\scenes\mws_wat_02.scene` / scene / 139 -> 109 -> 251 |
| `42f7e3c15584a99b1bf8` | 3 | `base\open_world\mini_world_stories\watson\mws_wat_02\scenes\mws_wat_02.scene` / scene / 111 -> 147 -> 242 |
| `10928bf3a09bffffa44f` | 2 | `base\open_world\mini_world_stories\watson\mws_wat_02\mws_wat_02.questphase` / h20 / 0 -> 7 -> 19 |
| `5f0386b39f7a796a5e89` | 2 | `base\open_world\mini_world_stories\watson\mws_wat_02\mws_wat_02.questphase` / h0 / 61 -> 62 -> 59 |
| `a487200a203e0fceee90` | 2 | `base\open_world\mini_world_stories\watson\mws_wat_02\scenes\mws_wat_02.scene` / scene / 9 -> 12 -> 371 |
| `c6429da14d612e3eb7a7` | 2 | `base\open_world\mini_world_stories\watson\mws_wat_02\scenes\mws_wat_02.scene` / scene / 146 -> 651 -> 635 |
| `cbdd7cfb60a9758fd17c` | 2 | `base\open_world\mini_world_stories\watson\mws_wat_02\scenes\mws_wat_02.scene` / scene / 396 -> 146 -> 651 |
| `d883fdc288ad16def783` | 2 | `base\open_world\mini_world_stories\watson\mws_wat_02\scenes\mws_wat_02.scene` / scene / 396 -> 146 -> 163 |
| `da75b9e935b9ef247755` | 2 | `base\open_world\mini_world_stories\watson\mws_wat_02\scenes\mws_wat_02.scene` / scene / 258 -> 146 -> 163 |
| `01851cd592743a0d6b6d` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_02\mws_wat_02.questphase` / h0 / 56 -> 17 -> 20 |
| `036fe2ef7dfcd7dfb400` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_02\mws_wat_02.questphase` / h0 / 33 -> 38 -> 41 |
| `05d2345367007644492b` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_02\mws_wat_02.questphase` / h20 / 26 -> 29 -> 28 |
| `06ef05080eff6dba3232` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_02\mws_wat_02.questphase` / h20 / 27 -> 24 -> 25 |
| `07a508d9181a1ec44ac6` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_02\mws_wat_02.quest` / h0 / 4 -> 5 -> 2 |
| `09b1be5198db8be1af8b` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_02\scenes\mws_wat_02.scene` / scene / 101 -> 194 -> 396 |
| `0a4d54e2e01ca01cf868` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_02\scenes\mws_wat_02.scene` / scene / 1 -> 61 -> 38 |
| `0af14be79ea9d211ac55` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_02\scenes\mws_wat_02.scene` / scene / 510 -> 541 -> 213 |
| `0b89f1ac37be17100008` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_02\mws_wat_02.questphase` / h0 / 58 -> 61 -> 62 |
| `0c7e3a1afd6e8dd9934f` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_02\scenes\mws_wat_02.scene` / scene / 560 -> 573 -> 574 |
| `0ff0b50b965a72448608` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_02\scenes\mws_wat_02.scene` / scene / 663 -> 553 -> 551 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
