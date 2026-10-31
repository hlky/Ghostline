# base-mws-se5-06

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\mini_world_stories\badlands\se5\mws_se5_06\communities\mws_se5_06_com_netwatch.community` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\badlands\se5\mws_se5_06\mws_se5_06.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\badlands\se5\mws_se5_06\mws_se5_06.quest` | content candidate | 1 / 0 | base\open_world\mini_world_stories\badlands\se5\mws_se5_06\mws_se5_06.questphase |
| `base\open_world\mini_world_stories\badlands\se5\mws_se5_06\mws_se5_06.questphase` | content candidate | 4 / 0 | base\open_world\mini_world_stories\badlands\se5\mws_se5_06\scenes\mws_se5_06.scene |
| `base\open_world\mini_world_stories\badlands\se5\mws_se5_06\scenes\mws_se5_06.scene` | content candidate | 0 / 3 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questTriggerCondition]` | 1 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questCutControlNodeDefinition` | 2 |
| `questEndNodeDefinition` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 16 |
| `questInputNodeDefinition` | 4 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questLogicalAndNodeDefinition` | 1 |
| `questLogicalHubNodeDefinition` | 5 |
| `questMiscAICommandNode` | 3 |
| `questOutputNodeDefinition` | 5 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam,questLogicalCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 7 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questGameTimeDelay_ConditionType,questLogicalCondition,questObjectDistance,questTimeCondition,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questTriggerCondition,questVarComparison_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 8 |
| `questPauseConditionNodeDefinition[questTickDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 2 |
| `questPhaseNodeDefinition` | 3 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 8 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 6 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 2 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 6 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 1 |
| `scnStartNode[scnNodeId]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `40a2b91d95d91657625a` | 6 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_06\mws_se5_06.questphase` / h89 / 88 -> 87 -> 100 |
| `64bc6000dbc1b2d6022c` | 6 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_06\mws_se5_06.questphase` / h89 / 87 -> 100 -> 70 |
| `77f247ea44c539796820` | 6 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_06\mws_se5_06.questphase` / h89 / 0 -> 88 -> 87 |
| `bfb5e61140052ae80179` | 6 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_06\mws_se5_06.questphase` / h89 / 100 -> 70 -> 94 |
| `9af8a87f20a910659fa8` | 4 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_06\mws_se5_06.questphase` / h22 / 60 -> 61 -> 62 |
| `249fc6a7f09c7e4fdf77` | 2 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_06\mws_se5_06.questphase` / h89 / 68 -> 71 -> 72 |
| `712181018bbb3a6196bc` | 2 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_06\mws_se5_06.questphase` / h89 / 73 -> 68 -> 71 |
| `79ff30ab7464b071eda5` | 2 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_06\mws_se5_06.questphase` / h22 / 16 -> 39 -> 41 |
| `96b6c6c49d999f2f6156` | 2 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_06\mws_se5_06.questphase` / h22 / 35 -> 11 -> 16 |
| `bfe95df47bd1ca67330f` | 2 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_06\mws_se5_06.questphase` / h22 / 44 -> 27 -> 35 |
| `e7f4dab64cf88a718cc9` | 2 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_06\mws_se5_06.questphase` / h22 / 34 -> 26 -> 2 |
| `ff01e9ceea872dacf574` | 2 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_06\mws_se5_06.questphase` / h22 / 11 -> 16 -> 39 |
| `00c3ca0ac0b55db639ca` | 1 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_06\mws_se5_06.questphase` / h22 / 56 -> 66 -> 59 |
| `00dcd95c58bd6418a1dd` | 1 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_06\mws_se5_06.questphase` / h22 / 13 -> 56 -> 66 |
| `0a3c26d6b894818cf6fa` | 1 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_06\mws_se5_06.questphase` / h22 / 49 -> 36 -> 43 |
| `1706a53841ab6c8bfd0d` | 1 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_06\mws_se5_06.questphase` / h22 / 47 -> 57 -> 56 |
| `19775f0069af02d420b8` | 1 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_06\mws_se5_06.questphase` / h22 / 57 -> 56 -> 66 |
| `215ca95d939006973a7d` | 1 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_06\mws_se5_06.questphase` / h22 / 64 -> 65 -> 58 |
| `237687944a84dd96b7b5` | 1 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_06\mws_se5_06.questphase` / h626 / 0 -> 9 -> 10 |
| `291b06b201e0ead1e4bb` | 1 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_06\mws_se5_06.questphase` / h0 / 4 -> 5 -> 2 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
