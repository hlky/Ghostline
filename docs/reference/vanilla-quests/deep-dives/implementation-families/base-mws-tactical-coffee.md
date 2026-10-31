# base-mws-tactical-coffee

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\mini_world_stories\watson\mws_tactical_coffee\communities\tactical_coffee_comm.community` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\watson\mws_tactical_coffee\nws_phase_test.questphase` | content candidate | 1 / 0 |  |
| `base\open_world\mini_world_stories\watson\mws_tactical_coffee\nws_tactical_coffee_def.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\watson\mws_tactical_coffee\nws_tactical_coffee_quest.quest` | content candidate | 1 / 0 | base\open_world\mini_world_stories\watson\mws_tactical_coffee\nws_phase_test.questphase |
| `base\open_world\mini_world_stories\watson\mws_tactical_coffee\scene\nws_tactical_coffee_scene.scene` | content candidate | 0 / 20 |  |
| `base\open_world\mini_world_stories\watson\mws_tactical_coffee\scene\tactical_coffee_scene.scene` | content candidate | 0 / 30 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioParameterNodeType]` | 3 |
| `questAudioNodeDefinition[questAudioSwitchNodeType]` | 3 |
| `questDeletionMarkerNodeDefinition` | 5 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 2 |
| `questInputNodeDefinition` | 1 |
| `questLogicalAndNodeDefinition` | 1 |
| `questLogicalHubNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 2 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 5 |
| `questPauseConditionNodeDefinition[questTimeSkipped_ConditionType,questUICondition]` | 1 |
| `questPhaseNodeDefinition` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 65 |
| `questStartNodeDefinition` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 2 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 3 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 2 |
| `scnDeletionMarkerNode[scnNodeId]` | 18 |
| `scnStartNode[scnNodeId]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `20a77143a898bc753a26` | 17 | `base\open_world\mini_world_stories\watson\mws_tactical_coffee\nws_phase_test.questphase` / h0 / 211 -> 212 -> 213 |
| `5b9256fd6f1edd20bf9c` | 13 | `base\open_world\mini_world_stories\watson\mws_tactical_coffee\scene\tactical_coffee_scene.scene` / scene / 9 -> 10 -> 11 |
| `8a9ccef8cd6f64f786a9` | 8 | `base\open_world\mini_world_stories\watson\mws_tactical_coffee\nws_phase_test.questphase` / h0 / 291 -> 202 -> 235 |
| `c1397719e132b2fe5425` | 8 | `base\open_world\mini_world_stories\watson\mws_tactical_coffee\nws_phase_test.questphase` / h0 / 202 -> 211 -> 212 |
| `7b96b99dfc9d7f5ed746` | 7 | `base\open_world\mini_world_stories\watson\mws_tactical_coffee\scene\tactical_coffee_scene.scene` / scene / 1 -> 12 -> 13 |
| `f7ae732f504e68ef12b1` | 7 | `base\open_world\mini_world_stories\watson\mws_tactical_coffee\scene\nws_tactical_coffee_scene.scene` / scene / 28 -> 19 -> 21 |
| `0567520353b696200994` | 1 | `base\open_world\mini_world_stories\watson\mws_tactical_coffee\nws_phase_test.questphase` / h0 / 284 -> 283 -> 282 |
| `0ad9f74a2d370ba01327` | 1 | `base\open_world\mini_world_stories\watson\mws_tactical_coffee\nws_phase_test.questphase` / h0 / 219 -> 262 -> 271 |
| `1972a0532f20a107c8bb` | 1 | `base\open_world\mini_world_stories\watson\mws_tactical_coffee\nws_phase_test.questphase` / h0 / 312 -> 432 -> 349 |
| `1fafc5a2aa2a1584d1a7` | 1 | `base\open_world\mini_world_stories\watson\mws_tactical_coffee\nws_phase_test.questphase` / h0 / 312 -> 330 -> 353 |
| `20d7e7055b4afb21dd89` | 1 | `base\open_world\mini_world_stories\watson\mws_tactical_coffee\nws_phase_test.questphase` / h0 / 232 -> 262 -> 271 |
| `220dd56eae6d91ef9d7d` | 1 | `base\open_world\mini_world_stories\watson\mws_tactical_coffee\nws_phase_test.questphase` / h0 / 201 -> 312 -> 284 |
| `25aae51001db85d5b1fb` | 1 | `base\open_world\mini_world_stories\watson\mws_tactical_coffee\nws_phase_test.questphase` / h0 / 283 -> 282 -> 257 |
| `380f2153d1639bdd0d26` | 1 | `base\open_world\mini_world_stories\watson\mws_tactical_coffee\nws_phase_test.questphase` / h0 / 228 -> 262 -> 271 |
| `3a2810c1411531a40959` | 1 | `base\open_world\mini_world_stories\watson\mws_tactical_coffee\nws_phase_test.questphase` / h0 / 237 -> 242 -> 262 |
| `48e9e4ccfc12d1aa0d84` | 1 | `base\open_world\mini_world_stories\watson\mws_tactical_coffee\nws_phase_test.questphase` / h0 / 212 -> 213 -> 262 |
| `55af3b45d87955fbf042` | 1 | `base\open_world\mini_world_stories\watson\mws_tactical_coffee\nws_phase_test.questphase` / h0 / 262 -> 271 -> 258 |
| `64638e13caa3d5c4d9e7` | 1 | `base\open_world\mini_world_stories\watson\mws_tactical_coffee\nws_phase_test.questphase` / h0 / 257 -> 291 -> 202 |
| `690ef6c1e05e92246fe2` | 1 | `base\open_world\mini_world_stories\watson\mws_tactical_coffee\nws_phase_test.questphase` / h0 / 227 -> 228 -> 262 |
| `6f9c516ab15d00fd0482` | 1 | `base\open_world\mini_world_stories\watson\mws_tactical_coffee\nws_phase_test.questphase` / h0 / 353 -> 366 -> 354 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
