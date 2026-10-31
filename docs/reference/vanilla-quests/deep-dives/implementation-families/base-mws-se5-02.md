# base-mws-se5-02

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\mini_world_stories\badlands\se5\mws_se5_02\community\mws_se5_02_run_away.community` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\badlands\se5\mws_se5_02\mws_se05_02.questphase` | content candidate | 2 / 0 |  |
| `base\open_world\mini_world_stories\badlands\se5\mws_se5_02\mws_se5_02.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\badlands\se5\mws_se5_02\mws_se5_02.quest` | content candidate | 1 / 0 | base\open_world\mini_world_stories\badlands\se5\mws_se5_02\mws_se05_02.questphase |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_Kill,questCharacterManagerCombat_NodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 1 |
| `questCheckpointNodeDefinition` | 1 |
| `questCombatNodeDefinition` | 2 |
| `questEndNodeDefinition` | 1 |
| `questEquipItemNodeDefinition[questEquipItemParams,questObservableUniversalRef]` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 2 |
| `questInputNodeDefinition` | 4 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questLogicalAndNodeDefinition` | 2 |
| `questOutputNodeDefinition` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 6 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleSpawned_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleSpeed_ConditionType]` | 1 |
| `questPhaseNodeDefinition` | 1 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 3 |
| `questStartNodeDefinition` | 1 |
| `questUIManagerNodeDefinition[questDisplayMessageBox_NodeType]` | 1 |
| `questVehicleNodeDefinition[questSetImmovable_NodeType]` | 2 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 4 |
| `questVoicesetManagerNodeDefinition[questChangeVoicesetState_NodeType,questChangeVoicesetState_NodeTypeParams]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `2251a3c44ea8a153bc79` | 2 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_02\mws_se05_02.questphase` / h2 / 2 -> 6 -> 3 |
| `918483d69e9690ef41d0` | 2 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_02\mws_se05_02.questphase` / h2 / 4 -> 9 -> 8 |
| `a829d325c5df5f2cd6e0` | 2 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_02\mws_se05_02.questphase` / h2 / 7 -> 39 -> 42 |
| `01851cd592743a0d6b6d` | 1 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_02\mws_se05_02.questphase` / h0 / 46 -> 42 -> 34 |
| `131a9aaeed1317f9415f` | 1 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_02\mws_se05_02.questphase` / h0 / 43 -> 34 -> 44 |
| `199cbb3a2046091ad073` | 1 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_02\mws_se05_02.questphase` / h2 / 37 -> 33 -> 34 |
| `2179483c4d9ed5db29c9` | 1 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_02\mws_se05_02.questphase` / h0 / 41 -> 46 -> 42 |
| `268d903f66cc5cb4112b` | 1 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_02\mws_se05_02.questphase` / h2 / 9 -> 12 -> 5 |
| `28545b5893ed55a6c748` | 1 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_02\mws_se05_02.questphase` / h2 / 5 -> 37 -> 33 |
| `328b5333583932d21404` | 1 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_02\mws_se05_02.questphase` / h2 / 16 -> 17 -> 14 |
| `35e8676ac0e5808d43fa` | 1 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_02\mws_se05_02.questphase` / h2 / 7 -> 12 -> 5 |
| `40a2b94665015716ee55` | 1 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_02\mws_se05_02.questphase` / h2 / 12 -> 5 -> 37 |
| `41ed42abf293f6abf5f2` | 1 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_02\mws_se05_02.questphase` / h2 / 6 -> 4 -> 9 |
| `6043637a30ab8b7d920c` | 1 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_02\mws_se05_02.questphase` / h2 / 7 -> 12 -> 20 |
| `72456e8dd927fd679172` | 1 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_02\mws_se05_02.questphase` / h2 / 3 -> 7 -> 12 |
| `7c4d6476f00dc04621ba` | 1 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_02\mws_se05_02.questphase` / h2 / 31 -> 11 -> 19 |
| `7e0dde0d6ba87cd70081` | 1 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_02\mws_se05_02.questphase` / h2 / 4 -> 9 -> 12 |
| `8948371b5f0a203cc0f3` | 1 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_02\mws_se05_02.questphase` / h2 / 39 -> 43 -> 45 |
| `8d10896873df5c62014e` | 1 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_02\mws_se05_02.questphase` / h2 / 3 -> 7 -> 39 |
| `94befa2ac2773186b28b` | 1 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_02\mws_se05_02.questphase` / h2 / 33 -> 34 -> 32 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
