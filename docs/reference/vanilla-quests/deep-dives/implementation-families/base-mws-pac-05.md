# base-mws-pac-05

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\mini_world_stories\pacifica\mws_pac_05\community\mws_pac_05_community.community` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\pacifica\mws_pac_05\mws_pac_05.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\pacifica\mws_pac_05\mws_pac_05.quest` | content candidate | 1 / 0 | base\open_world\mini_world_stories\pacifica\mws_pac_05\mws_pac_05.questphase |
| `base\open_world\mini_world_stories\pacifica\mws_pac_05\mws_pac_05.questphase` | content candidate | 3 / 0 | base\open_world\mini_world_stories\pacifica\mws_pac_05\scenes\mws_pac_05.scene |
| `base\open_world\mini_world_stories\pacifica\mws_pac_05\scenes\mws_pac_05.scene` | content candidate | 0 / 4 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 2 |
| `questCombatNodeDefinition` | 1 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 2 |
| `questEndNodeDefinition` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 3 |
| `questInputNodeDefinition` | 4 |
| `questLogicalHubNodeDefinition` | 2 |
| `questOutputNodeDefinition` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterEquippedItem_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questFactsDBCondition,questInventory_ConditionType,questLogicalCondition,questObjectCondition,questObjectDistance,questUniversalRef,questValueDistance,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 3 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 2 |
| `questPhaseNodeDefinition` | 3 |
| `questSceneNodeDefinition[scnWorldMarker]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 3 |
| `questStartNodeDefinition` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 2 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 1 |
| `scnEndNode[scnNodeId]` | 1 |
| `scnStartNode[scnNodeId]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `0055fad2e9937ce40ea3` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_05\mws_pac_05.questphase` / h24 / 21 -> 24 -> 1 |
| `1eb39b7557e061a7db8a` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_05\mws_pac_05.questphase` / h24 / 0 -> 21 -> 24 |
| `2e04a620886c7d6307a9` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_05\mws_pac_05.questphase` / h24 / 14 -> 15 -> 16 |
| `2e0739466609a56fbf77` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_05\mws_pac_05.questphase` / h24 / 2 -> 13 -> 12 |
| `328b5333583932d21404` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_05\mws_pac_05.questphase` / h210 / 0 -> 2 -> 1 |
| `4dd95af11480f4a5b13a` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_05\scenes\mws_pac_05.scene` / scene / 1 -> 4 -> 10 |
| `53546007e449fd457df4` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_05\mws_pac_05.questphase` / h0 / 36 -> 39 -> 20 |
| `7672e1478f3416201567` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_05\mws_pac_05.questphase` / h24 / 14 -> 15 -> 2 |
| `7d207526a879bbe33293` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_05\mws_pac_05.questphase` / h24 / 15 -> 2 -> 13 |
| `a68010d462e7ee729e14` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_05\mws_pac_05.questphase` / h0 / 39 -> 20 -> 36 |
| `ad1d14320e93765feb0b` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_05\scenes\mws_pac_05.scene` / scene / 4 -> 10 -> 2 |
| `cfdc4d160cbda67f5eb4` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_05\mws_pac_05.questphase` / h24 / 0 -> 14 -> 15 |
| `eee5adb4761257214b1f` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_05\mws_pac_05.questphase` / h0 / 20 -> 36 -> 39 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
