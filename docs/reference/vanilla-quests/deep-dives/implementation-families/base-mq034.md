# base-mq034

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\quest\bugfixing\minor_quests\mq034\mq034_cinematic_bugfixes.questphase` | repair | 2 / 0 |  |
| `base\quest\bugfixing\minor_quests\mq034\mq034_quest_bugfixes.questphase` | repair | 2 / 0 |  |
| `base\quest\minor_quests\mq034\communities\mq034_com_stash.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq034\mq034_stash.gamedef` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq034\mq034_stash.quest` | content candidate | 2 / 0 | base\quest\minor_quests\mq034\mq034_stash.questphase |
| `base\quest\minor_quests\mq034\mq034_stash.questphase` | content candidate | 4 / 0 | base\quest\minor_quests\mq034\phases\mq034_cleanup.questphase; base\quest\minor_quests\mq034\phases\mq034_quest.questphase; base\quest\minor_quests\mq034\phases\mq034_setup.questphase |
| `base\quest\minor_quests\mq034\phases\mq034_cleanup.questphase` | content candidate | 1 / 0 |  |
| `base\quest\minor_quests\mq034\phases\mq034_quest.questphase` | content candidate | 1 / 0 |  |
| `base\quest\minor_quests\mq034\phases\mq034_setup.questphase` | content candidate | 1 / 0 |  |
| `base\quest\minor_quests\mq034\scenes\mq034_01_scene.scene` | content candidate | 0 / 16 |  |
| `base\quest\minor_quests\mq034\scenes\mq034_xx_debug.scene` | content candidate | 0 / 2 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questEndNodeDefinition` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 2 |
| `questInputNodeDefinition` | 12 |
| `questLogicalAndNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 10 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 1 |
| `questPhaseNodeDefinition` | 7 |
| `questStartNodeDefinition` | 1 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 2 |
| `scnChoiceNode[scnChoiceNodeNsAttachToGameObjectParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 2 |
| `scnEndNode[scnNodeId]` | 8 |
| `scnStartNode[scnNodeId]` | 8 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `0e8f622afa242001778b` | 2 | `base\quest\minor_quests\mq034\scenes\mq034_01_scene.scene` / scene / 38 -> 40 -> 39 |
| `9c634ff27b9a7aa77918` | 2 | `base\quest\bugfixing\minor_quests\mq034\mq034_cinematic_bugfixes.questphase` / h0 / 0 -> 10 -> 5 |
| `1a60a7b0aaace14e895f` | 1 | `base\quest\minor_quests\mq034\phases\mq034_quest.questphase` / h0 / 34 -> 35 -> 1 |
| `31f9c37e5463d5e809b6` | 1 | `base\quest\minor_quests\mq034\phases\mq034_cleanup.questphase` / h0 / 0 -> 5 -> 6 |
| `7c6bd5c4ae26723cb30e` | 1 | `base\quest\minor_quests\mq034\phases\mq034_quest.questphase` / h0 / 0 -> 33 -> 34 |
| `e87a300fde63e7545752` | 1 | `base\quest\minor_quests\mq034\phases\mq034_cleanup.questphase` / h0 / 5 -> 6 -> 1 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
