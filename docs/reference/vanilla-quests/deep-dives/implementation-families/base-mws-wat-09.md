# base-mws-wat-09

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\mini_world_stories\watson\mws_wat_09\communities\mws_wat_09.community` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\watson\mws_wat_09\mws_wat_09.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\watson\mws_wat_09\mws_wat_09.quest` | content candidate | 1 / 0 | base\open_world\mini_world_stories\watson\mws_wat_09\mws_wat_09.questphase |
| `base\open_world\mini_world_stories\watson\mws_wat_09\mws_wat_09.questphase` | content candidate | 6 / 0 | base\open_world\mini_world_stories\watson\mws_wat_09\scenes\mws_wat_09.scene |
| `base\open_world\mini_world_stories\watson\mws_wat_09\scenes\mws_wat_09.scene` | content candidate | 0 / 5 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_Kill,questCharacterManagerCombat_NodeType]` | 3 |
| `questDeletionMarkerNodeDefinition` | 4 |
| `questEndNodeDefinition` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 1 |
| `questGameManagerNodeDefinition[questGameplayRestrictions_NodeType]` | 3 |
| `questInputNodeDefinition` | 8 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 3 |
| `questOutputNodeDefinition` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questPhaseNodeDefinition` | 5 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 3 |
| `questStartNodeDefinition` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 2 |
| `scnEndNode[scnNodeId]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 2 |
| `scnStartNode[scnNodeId]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `4dd2c6eb79b7fb144498` | 2 | `base\open_world\mini_world_stories\watson\mws_wat_09\mws_wat_09.questphase` / h109 / 2 -> 3 -> 4 |
| `cf5fd5edd6bef146b540` | 2 | `base\open_world\mini_world_stories\watson\mws_wat_09\mws_wat_09.questphase` / h144 / 0 -> 13 -> 14 |
| `fc487b3eb8a7371b61cc` | 2 | `base\open_world\mini_world_stories\watson\mws_wat_09\mws_wat_09.questphase` / h109 / 5 -> 2 -> 3 |
| `0b487c56874911c2ea72` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_09\scenes\mws_wat_09.scene` / scene / 5 -> 10 -> 8 |
| `1e253d0fcbd364975401` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_09\mws_wat_09.questphase` / h39 / 27 -> 25 -> 26 |
| `5c22cbe05ce147d543b4` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_09\mws_wat_09.questphase` / h0 / 5 -> 4 -> 1 |
| `72e6d462116736c0cd5f` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_09\scenes\mws_wat_09.scene` / scene / 10 -> 8 -> 1 |
| `804cb97c944e3c3bf436` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_09\mws_wat_09.questphase` / h39 / 0 -> 27 -> 25 |
| `91273c6fdde2220acfaf` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_09\mws_wat_09.questphase` / h18 / 72 -> 70 -> 61 |
| `98c4c551cf2b64dd4162` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_09\mws_wat_09.questphase` / h18 / 0 -> 59 -> 7 |
| `9bcefd0d8dbfc24fb456` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_09\mws_wat_09.questphase` / h109 / 0 -> 2 -> 3 |
| `a9054c711a21d83baa7b` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_09\mws_wat_09.questphase` / h39 / 16 -> 9 -> 1 |
| `b03258d0a340d6fea3e4` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_09\mws_wat_09.questphase` / h39 / 15 -> 16 -> 9 |
| `b2e755d9b945082af824` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_09\mws_wat_09.questphase` / h0 / 3 -> 4 -> 1 |
| `b767a7454011844ebdac` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_09\mws_wat_09.questphase` / h39 / 26 -> 15 -> 16 |
| `bb4cbad40b0dd9e26485` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_09\mws_wat_09.questphase` / h18 / 59 -> 7 -> 56 |
| `bceded3ff27b27417970` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_09\mws_wat_09.questphase` / h18 / 70 -> 61 -> 1 |
| `c30466373ad2bc276d56` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_09\mws_wat_09.questphase` / h217 / 6 -> 5 -> 4 |
| `d04d84da5e5daa1203fa` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_09\mws_wat_09.questphase` / h217 / 5 -> 4 -> 1 |
| `d84f2b81bc7e375e0e19` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_09\mws_wat_09.questphase` / h217 / 2 -> 6 -> 5 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
