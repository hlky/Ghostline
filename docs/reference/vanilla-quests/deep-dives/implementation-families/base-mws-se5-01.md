# base-mws-se5-01

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\mini_world_stories\badlands\se5\mws_se5_01\community\mws_se5_01_burning_man.community` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\badlands\se5\mws_se5_01\mws_se5_01.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\badlands\se5\mws_se5_01\mws_se5_01.quest` | content candidate | 1 / 0 | base\open_world\mini_world_stories\badlands\se5\mws_se5_01\mws_se5_01.questphase |
| `base\open_world\mini_world_stories\badlands\se5\mws_se5_01\mws_se5_01.questphase` | content candidate | 3 / 0 | base\open_world\mini_world_stories\badlands\se5\mws_se5_01\scenes\mws_se5_01.scene |
| `base\open_world\mini_world_stories\badlands\se5\mws_se5_01\scenes\mws_se5_01.scene` | content candidate | 0 / 6 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_Kill,questCharacterManagerCombat_NodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 1 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 4 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 1 |
| `questInputNodeDefinition` | 5 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 4 |
| `questLogicalAndNodeDefinition` | 1 |
| `questLogicalHubNodeDefinition` | 4 |
| `questLogicalXorNodeDefinition` | 5 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 4 |
| `questOutputNodeDefinition` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterStatusEffect_CondtionType]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questTimeCondition,questTimePeriod_ConditionType,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 6 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 6 |
| `questPhaseNodeDefinition` | 2 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 5 |
| `questStartNodeDefinition` | 1 |
| `questSwitchNodeDefinition[questConditionItem,questTriggerCondition]` | 1 |
| `questUIManagerNodeDefinition[questDisplayMessageBox_NodeType]` | 1 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 1 |
| `scnEndNode[scnNodeId]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 2 |
| `scnStartNode[scnNodeId]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `32c3a8dde8c0a9064338` | 4 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_01\mws_se5_01.questphase` / h43 / 10 -> 39 -> 24 |
| `a3482bab3b385654b21b` | 4 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_01\mws_se5_01.questphase` / h43 / 24 -> 40 -> 22 |
| `e61f6e404458ce3701ec` | 4 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_01\mws_se5_01.questphase` / h43 / 3 -> 12 -> 10 |
| `f24d5f1a55518f5cbb7c` | 4 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_01\mws_se5_01.questphase` / h43 / 39 -> 41 -> 40 |
| `f768770776ef1496513d` | 4 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_01\mws_se5_01.questphase` / h43 / 39 -> 24 -> 40 |
| `0055fad2e9937ce40ea3` | 1 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_01\mws_se5_01.questphase` / h12 / 58 -> 35 -> 3 |
| `0944617c11622371a968` | 1 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_01\mws_se5_01.questphase` / h12 / 2 -> 9 -> 47 |
| `131a9aaeed1317f9415f` | 1 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_01\mws_se5_01.questphase` / h0 / 79 -> 76 -> 1 |
| `135160f00535b1d5e265` | 1 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_01\scenes\mws_se5_01.scene` / scene / 4 -> 10 -> 14 |
| `328b5333583932d21404` | 1 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_01\mws_se5_01.questphase` / h12 / 34 -> 35 -> 3 |
| `55d38883823a038a8558` | 1 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_01\mws_se5_01.questphase` / h43 / 22 -> 9 -> 23 |
| `658fe17f8b47d2c016b7` | 1 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_01\mws_se5_01.questphase` / h43 / 0 -> 34 -> 1 |
| `72e6d462116736c0cd5f` | 1 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_01\scenes\mws_se5_01.scene` / scene / 14 -> 11 -> 2 |
| `915266aa1e4c6b0b964a` | 1 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_01\scenes\mws_se5_01.scene` / scene / 1 -> 4 -> 10 |
| `a8e35e6b1e882ca98084` | 1 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_01\scenes\mws_se5_01.scene` / scene / 10 -> 14 -> 11 |
| `b2e755d9b945082af824` | 1 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_01\mws_se5_01.questphase` / h0 / 78 -> 76 -> 1 |
| `db9e46be876238846c13` | 1 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_01\mws_se5_01.questphase` / h43 / 9 -> 23 -> 1 |
| `e514ae000bb58f7fc0a8` | 1 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_01\mws_se5_01.questphase` / h0 / 0 -> 78 -> 76 |
| `f724959f5f95b3f8270e` | 1 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_01\mws_se5_01.questphase` / h43 / 11 -> 23 -> 1 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
