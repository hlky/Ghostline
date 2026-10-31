# base-mws-hey-02

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\mini_world_stories\heywood\mws_hey_02\characters\mws_hey_02.community` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\heywood\mws_hey_02\mws_hey_02.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\heywood\mws_hey_02\mws_hey_02.quest` | content candidate | 1 / 0 | base\open_world\mini_world_stories\heywood\mws_hey_02\mws_hey_02.questphase |
| `base\open_world\mini_world_stories\heywood\mws_hey_02\mws_hey_02.questphase` | content candidate | 2 / 0 | base\open_world\mini_world_stories\heywood\mws_hey_02\scenes\mws_hey_02_scene.scene |
| `base\open_world\mini_world_stories\heywood\mws_hey_02\scenes\mws_hey_02_scene.scene` | content candidate | 0 / 24 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questCutControlNodeDefinition` | 1 |
| `questEndNodeDefinition` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 4 |
| `questGameManagerNodeDefinition[questGameplayRestrictions_NodeType]` | 4 |
| `questInputNodeDefinition` | 4 |
| `questItemManagerNodeDefinition[questAddRemoveItem_NodeType,questAddRemoveItem_NodeTypeParams,questUniversalRef]` | 2 |
| `questOutputNodeDefinition` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 3 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPhaseNodeDefinition` | 1 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questPuppetAIManagerNodeDefinition[questPuppetAIManagerNodeDefinitionEntry]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 3 |
| `questStartNodeDefinition` | 1 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 3 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 2 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 2 |
| `scnAndNode[scnNodeId]` | 1 |
| `scnChoiceNode[questInventory_ConditionType,questObjectCondition,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnEndNode[scnNodeId]` | 1 |
| `scnHubNode[scnNodeId]` | 2 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 6 |
| `scnStartNode[scnNodeId]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `2ac8c63107064d2688af` | 2 | `base\open_world\mini_world_stories\heywood\mws_hey_02\mws_hey_02.questphase` / h12 / 9 -> 10 -> 8 |
| `2d3003e1c9407caa1c41` | 2 | `base\open_world\mini_world_stories\heywood\mws_hey_02\scenes\mws_hey_02_scene.scene` / scene / 9 -> 15 -> 19 |
| `3891697df227841b65f5` | 2 | `base\open_world\mini_world_stories\heywood\mws_hey_02\mws_hey_02.questphase` / h12 / 8 -> 12 -> 13 |
| `7686b27f9a892b69ef5d` | 2 | `base\open_world\mini_world_stories\heywood\mws_hey_02\mws_hey_02.questphase` / h12 / 12 -> 13 -> 7 |
| `a670b5774f03d88ee092` | 2 | `base\open_world\mini_world_stories\heywood\mws_hey_02\mws_hey_02.questphase` / h12 / 10 -> 13 -> 7 |
| `b48a0de3dd4cd342df90` | 2 | `base\open_world\mini_world_stories\heywood\mws_hey_02\mws_hey_02.questphase` / h12 / 10 -> 12 -> 13 |
| `d9cdd14827cb8e3ac949` | 2 | `base\open_world\mini_world_stories\heywood\mws_hey_02\mws_hey_02.questphase` / h12 / 9 -> 10 -> 7 |
| `137d9bb22d6889eb879c` | 1 | `base\open_world\mini_world_stories\heywood\mws_hey_02\mws_hey_02.questphase` / h12 / 9 -> 10 -> 11 |
| `21a4acd17f9d4fbf17c9` | 1 | `base\open_world\mini_world_stories\heywood\mws_hey_02\scenes\mws_hey_02_scene.scene` / scene / 19 -> 39 -> 35 |
| `3b0955fa5a1cdef30814` | 1 | `base\open_world\mini_world_stories\heywood\mws_hey_02\mws_hey_02.questphase` / h12 / 5 -> 7 -> 8 |
| `5345305d748c8a45459b` | 1 | `base\open_world\mini_world_stories\heywood\mws_hey_02\mws_hey_02.questphase` / h0 / 0 -> 3 -> 2 |
| `56d3bf3b08647544fbca` | 1 | `base\open_world\mini_world_stories\heywood\mws_hey_02\scenes\mws_hey_02_scene.scene` / scene / 15 -> 19 -> 21 |
| `590dd4c30ae7341e6669` | 1 | `base\open_world\mini_world_stories\heywood\mws_hey_02\mws_hey_02.questphase` / h12 / 8 -> 9 -> 10 |
| `5c22cbe05ce147d543b4` | 1 | `base\open_world\mini_world_stories\heywood\mws_hey_02\mws_hey_02.questphase` / h0 / 6 -> 2 -> 1 |
| `6a353fd4cdca12b560b7` | 1 | `base\open_world\mini_world_stories\heywood\mws_hey_02\mws_hey_02.questphase` / h12 / 18 -> 14 -> 1 |
| `70bf70c15a0db104bd22` | 1 | `base\open_world\mini_world_stories\heywood\mws_hey_02\scenes\mws_hey_02_scene.scene` / scene / 17 -> 44 -> 28 |
| `7eece6022ec117da8ee6` | 1 | `base\open_world\mini_world_stories\heywood\mws_hey_02\mws_hey_02.questphase` / h0 / 3 -> 2 -> 1 |
| `84e117da4660bbb4725b` | 1 | `base\open_world\mini_world_stories\heywood\mws_hey_02\scenes\mws_hey_02_scene.scene` / scene / 1 -> 6 -> 9 |
| `8628803ff3e19014c4aa` | 1 | `base\open_world\mini_world_stories\heywood\mws_hey_02\scenes\mws_hey_02_scene.scene` / scene / 73 -> 23 -> 60 |
| `92ec814dfd5d374be4d5` | 1 | `base\open_world\mini_world_stories\heywood\mws_hey_02\scenes\mws_hey_02_scene.scene` / scene / 39 -> 35 -> 23 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
