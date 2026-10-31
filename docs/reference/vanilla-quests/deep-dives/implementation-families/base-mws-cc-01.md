# base-mws-cc-01

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\mini_world_stories\city_center\mws_cc_01\community\mws_cc_01_vending_shock.community` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\city_center\mws_cc_01\mws_cc_01_vending_shock.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\city_center\mws_cc_01\mws_cc_01_vending_shock.quest` | content candidate | 1 / 0 | base\open_world\mini_world_stories\city_center\mws_cc_01\mws_cc_01_vending_shock.questphase |
| `base\open_world\mini_world_stories\city_center\mws_cc_01\mws_cc_01_vending_shock.questphase` | content candidate | 2 / 0 | base\open_world\mini_world_stories\city_center\mws_cc_01\scenes\mws_cc_01_vending_shock.scene |
| `base\open_world\mini_world_stories\city_center\mws_cc_01\scenes\mws_cc_01_vending_shock.scene` | content candidate | 0 / 8 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_Kill,questCharacterManagerCombat_NodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_ModifyHealth,questCharacterManagerCombat_NodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 2 |
| `questCutControlNodeDefinition` | 1 |
| `questDeletionMarkerNodeDefinition` | 1 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 6 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 1 |
| `questInputNodeDefinition` | 4 |
| `questItemManagerNodeDefinition[questAddRemoveItem_NodeType,questAddRemoveItem_NodeTypeParams,questUniversalRef]` | 12 |
| `questLogicalHubNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 2 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questSystemCondition,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 6 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 5 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 1 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questPuppetAIManagerNodeDefinition[questPuppetAIManagerNodeDefinitionEntry]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questUIManagerNodeDefinition[questWarningMessage_NodeType]` | 1 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 1 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 5 |
| `scnEndNode[scnNodeId]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 1 |
| `scnStartNode[scnNodeId]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `60afc4ed60743102c7b8` | 6 | `base\open_world\mini_world_stories\city_center\mws_cc_01\mws_cc_01_vending_shock.questphase` / h18 / 145 -> 151 -> 98 |
| `6bade9a6171d604fd6d8` | 3 | `base\open_world\mini_world_stories\city_center\mws_cc_01\mws_cc_01_vending_shock.questphase` / h18 / 199 -> 171 -> 172 |
| `7b44344c01ad5161d3ff` | 3 | `base\open_world\mini_world_stories\city_center\mws_cc_01\mws_cc_01_vending_shock.questphase` / h18 / 182 -> 171 -> 172 |
| `42d456f68cbe3d8345c3` | 2 | `base\open_world\mini_world_stories\city_center\mws_cc_01\mws_cc_01_vending_shock.questphase` / h18 / 171 -> 172 -> 173 |
| `4b51840588658d028e9f` | 2 | `base\open_world\mini_world_stories\city_center\mws_cc_01\mws_cc_01_vending_shock.questphase` / h18 / 9 -> 199 -> 172 |
| `56c53a847765e20a971f` | 2 | `base\open_world\mini_world_stories\city_center\mws_cc_01\mws_cc_01_vending_shock.questphase` / h18 / 199 -> 172 -> 173 |
| `131a9aaeed1317f9415f` | 1 | `base\open_world\mini_world_stories\city_center\mws_cc_01\mws_cc_01_vending_shock.questphase` / h0 / 4 -> 3 -> 1 |
| `328b5333583932d21404` | 1 | `base\open_world\mini_world_stories\city_center\mws_cc_01\mws_cc_01_vending_shock.questphase` / h18 / 94 -> 93 -> 92 |
| `494408df54ad21f27d4e` | 1 | `base\open_world\mini_world_stories\city_center\mws_cc_01\mws_cc_01_vending_shock.questphase` / h18 / 5 -> 122 -> 9 |
| `54816df1391b4e72c690` | 1 | `base\open_world\mini_world_stories\city_center\mws_cc_01\scenes\mws_cc_01_vending_shock.scene` / scene / 1 -> 82 -> 13 |
| `842fb4f5eb176ff27d5c` | 1 | `base\open_world\mini_world_stories\city_center\mws_cc_01\mws_cc_01_vending_shock.questphase` / h18 / 122 -> 9 -> 199 |
| `8913bd2382f877e6b306` | 1 | `base\open_world\mini_world_stories\city_center\mws_cc_01\mws_cc_01_vending_shock.questphase` / h18 / 173 -> 204 -> 205 |
| `987122e5e2fcd167cf6c` | 1 | `base\open_world\mini_world_stories\city_center\mws_cc_01\mws_cc_01_vending_shock.questphase` / h18 / 2 -> 4 -> 208 |
| `a12138a3a146a35163df` | 1 | `base\open_world\mini_world_stories\city_center\mws_cc_01\mws_cc_01_vending_shock.questphase` / h18 / 95 -> 93 -> 92 |
| `a94dfa0a863488e27f45` | 1 | `base\open_world\mini_world_stories\city_center\mws_cc_01\mws_cc_01_vending_shock.questphase` / h18 / 4 -> 208 -> 187 |
| `ac8d19928e1461ae3404` | 1 | `base\open_world\mini_world_stories\city_center\mws_cc_01\mws_cc_01_vending_shock.questphase` / h18 / 2 -> 4 -> 5 |
| `b2e755d9b945082af824` | 1 | `base\open_world\mini_world_stories\city_center\mws_cc_01\mws_cc_01_vending_shock.questphase` / h0 / 2 -> 3 -> 1 |
| `c17ba4ca3671fae59af4` | 1 | `base\open_world\mini_world_stories\city_center\mws_cc_01\mws_cc_01_vending_shock.questphase` / h18 / 4 -> 5 -> 122 |
| `e4a00268f1c797c63284` | 1 | `base\open_world\mini_world_stories\city_center\mws_cc_01\mws_cc_01_vending_shock.questphase` / h18 / 204 -> 205 -> 196 |
| `e514ae000bb58f7fc0a8` | 1 | `base\open_world\mini_world_stories\city_center\mws_cc_01\mws_cc_01_vending_shock.questphase` / h0 / 0 -> 2 -> 3 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
