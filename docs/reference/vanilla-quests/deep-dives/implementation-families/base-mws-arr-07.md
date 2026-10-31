# base-mws-arr-07

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\mini_world_stories\santo_domingo\mws_arr_07\communities\mws_arr_07.community` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\santo_domingo\mws_arr_07\mws_arr_07.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\santo_domingo\mws_arr_07\mws_arr_07.quest` | content candidate | 1 / 0 | base\open_world\mini_world_stories\santo_domingo\mws_arr_07\mws_arr_07.questphase |
| `base\open_world\mini_world_stories\santo_domingo\mws_arr_07\mws_arr_07.questphase` | content candidate | 4 / 0 | base\open_world\mini_world_stories\santo_domingo\mws_arr_07\scenes\mws_arr_07.scene |
| `base\open_world\mini_world_stories\santo_domingo\mws_arr_07\scenes\mws_arr_07.scene` | content candidate | 0 / 8 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 3 |
| `questInputNodeDefinition` | 7 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 2 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questItemManagerNodeDefinition[questLootTokenManager_NodeType,questLootTokenManager_NodeTypeParams]` | 1 |
| `questLogicalHubNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 2 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 2 |
| `questPhaseNodeDefinition` | 3 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 4 |
| `scnEndNode[scnNodeId]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 2 |
| `scnStartNode[scnNodeId]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `0b487c56874911c2ea72` | 2 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_07\scenes\mws_arr_07.scene` / scene / 4 -> 18 -> 5 |
| `284bdb86131aa380ab85` | 2 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_07\scenes\mws_arr_07.scene` / scene / 22 -> 4 -> 18 |
| `7092cd74bbc127b1100a` | 2 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_07\mws_arr_07.questphase` / h28 / 18 -> 10 -> 44 |
| `056f65b5401e52f37bc4` | 1 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_07\mws_arr_07.questphase` / h110 / 0 -> 2 -> 3 |
| `076f338100bee6b3f46a` | 1 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_07\mws_arr_07.questphase` / h28 / 10 -> 49 -> 46 |
| `106f1abb5ebc0458cadf` | 1 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_07\mws_arr_07.questphase` / h0 / 18 -> 14 -> 1 |
| `29c49fd4924dc8fb79d8` | 1 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_07\mws_arr_07.questphase` / h110 / 3 -> 4 -> 5 |
| `30717bda14dca1d25af5` | 1 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_07\mws_arr_07.questphase` / h0 / 9 -> 12 -> 13 |
| `3de51e6fe8bd91ef54c9` | 1 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_07\mws_arr_07.questphase` / h58 / 3 -> 5 -> 4 |
| `48fbfd49617fbdae2512` | 1 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_07\mws_arr_07.questphase` / h58 / 4 -> 7 -> 6 |
| `4c060802cbe2070b4771` | 1 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_07\mws_arr_07.questphase` / h0 / 0 -> 5 -> 3 |
| `5b1e19f2154626b81e08` | 1 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_07\mws_arr_07.questphase` / h0 / 12 -> 13 -> 14 |
| `5c22cbe05ce147d543b4` | 1 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_07\mws_arr_07.questphase` / h0 / 2 -> 4 -> 1 |
| `6abd6ba14b7e35dfc300` | 1 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_07\mws_arr_07.questphase` / h28 / 0 -> 18 -> 10 |
| `805c85adc601217728c0` | 1 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_07\scenes\mws_arr_07.scene` / scene / 15 -> 4 -> 18 |
| `83fb4d41561b3c554413` | 1 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_07\mws_arr_07.questphase` / h110 / 4 -> 5 -> 1 |
| `842f5c541045bcde954d` | 1 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_07\mws_arr_07.questphase` / h0 / 13 -> 14 -> 1 |
| `91273c6fdde2220acfaf` | 1 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_07\mws_arr_07.questphase` / h28 / 49 -> 48 -> 20 |
| `987122e5e2fcd167cf6c` | 1 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_07\mws_arr_07.questphase` / h58 / 0 -> 2 -> 3 |
| `adb35b885aae85462082` | 1 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_07\scenes\mws_arr_07.scene` / scene / 1 -> 15 -> 4 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
