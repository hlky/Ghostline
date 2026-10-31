# base-mws-se1-01

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\mini_world_stories\badlands\se1\mws_se1_01\characters\mws_se1_01.community` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\badlands\se1\mws_se1_01\mws_se1_01.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\badlands\se1\mws_se1_01\mws_se1_01.quest` | content candidate | 1 / 0 | base\open_world\mini_world_stories\badlands\se1\mws_se1_01\mws_se1_01.questphase |
| `base\open_world\mini_world_stories\badlands\se1\mws_se1_01\mws_se1_01.questphase` | content candidate | 2 / 0 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_Kill,questCharacterManagerCombat_NodeType]` | 5 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAnimset]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 1 |
| `questConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questTimeCondition,questTimePeriod_ConditionType]` | 1 |
| `questCutControlNodeDefinition` | 2 |
| `questEndNodeDefinition` | 1 |
| `questEnvironmentManagerNodeDefinition[questPlayEnv_SetWeather]` | 3 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 5 |
| `questGameManagerNodeDefinition[questGameplayRestrictions_NodeType]` | 7 |
| `questInputNodeDefinition` | 4 |
| `questLogicalAndNodeDefinition` | 2 |
| `questLogicalHubNodeDefinition` | 5 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 3 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questSystemCondition,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 3 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 2 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questTimeCondition,questTimePeriod_ConditionType,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 8 |
| `questPauseConditionNodeDefinition[questTimeCondition,questTimePeriod_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questPhaseNodeDefinition` | 1 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 9 |
| `questStartNodeDefinition` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 5 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 4 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 7 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `0a555d691cabc1c8e666` | 4 | `base\open_world\mini_world_stories\badlands\se1\mws_se1_01\mws_se1_01.questphase` / h14 / 73 -> 12 -> 77 |
| `1b13f96c89356f971f2f` | 4 | `base\open_world\mini_world_stories\badlands\se1\mws_se1_01\mws_se1_01.questphase` / h14 / 18 -> 73 -> 12 |
| `e4a00268f1c797c63284` | 4 | `base\open_world\mini_world_stories\badlands\se1\mws_se1_01\mws_se1_01.questphase` / h14 / 9 -> 73 -> 12 |
| `2ac8c63107064d2688af` | 2 | `base\open_world\mini_world_stories\badlands\se1\mws_se1_01\mws_se1_01.questphase` / h14 / 43 -> 44 -> 42 |
| `3891697df227841b65f5` | 2 | `base\open_world\mini_world_stories\badlands\se1\mws_se1_01\mws_se1_01.questphase` / h14 / 47 -> 41 -> 42 |
| `7686b27f9a892b69ef5d` | 2 | `base\open_world\mini_world_stories\badlands\se1\mws_se1_01\mws_se1_01.questphase` / h14 / 41 -> 42 -> 46 |
| `a3e5f861a4b71433135a` | 2 | `base\open_world\mini_world_stories\badlands\se1\mws_se1_01\mws_se1_01.questphase` / h14 / 70 -> 40 -> 69 |
| `a670b5774f03d88ee092` | 2 | `base\open_world\mini_world_stories\badlands\se1\mws_se1_01\mws_se1_01.questphase` / h14 / 44 -> 42 -> 46 |
| `b48a0de3dd4cd342df90` | 2 | `base\open_world\mini_world_stories\badlands\se1\mws_se1_01\mws_se1_01.questphase` / h14 / 44 -> 41 -> 42 |
| `d9cdd14827cb8e3ac949` | 2 | `base\open_world\mini_world_stories\badlands\se1\mws_se1_01\mws_se1_01.questphase` / h14 / 43 -> 44 -> 41 |
| `e5b6cd11c476886c8553` | 2 | `base\open_world\mini_world_stories\badlands\se1\mws_se1_01\mws_se1_01.questphase` / h14 / 6 -> 17 -> 18 |
| `06171253673f1f94fee0` | 1 | `base\open_world\mini_world_stories\badlands\se1\mws_se1_01\mws_se1_01.questphase` / h14 / 38 -> 9 -> 73 |
| `0aaac32807f228484448` | 1 | `base\open_world\mini_world_stories\badlands\se1\mws_se1_01\mws_se1_01.questphase` / h14 / 38 -> 9 -> 68 |
| `0bb9f75b05008797b568` | 1 | `base\open_world\mini_world_stories\badlands\se1\mws_se1_01\mws_se1_01.questphase` / h14 / 60 -> 55 -> 61 |
| `10883942d8ed42b98d9a` | 1 | `base\open_world\mini_world_stories\badlands\se1\mws_se1_01\mws_se1_01.questphase` / h14 / 2 -> 3 -> 87 |
| `115bd5a61f0c0fefdccd` | 1 | `base\open_world\mini_world_stories\badlands\se1\mws_se1_01\mws_se1_01.questphase` / h14 / 60 -> 57 -> 61 |
| `137d9bb22d6889eb879c` | 1 | `base\open_world\mini_world_stories\badlands\se1\mws_se1_01\mws_se1_01.questphase` / h14 / 43 -> 44 -> 45 |
| `1553ea49805c9d5b4f24` | 1 | `base\open_world\mini_world_stories\badlands\se1\mws_se1_01\mws_se1_01.questphase` / h14 / 89 -> 87 -> 97 |
| `166921ac3df89cbe37bc` | 1 | `base\open_world\mini_world_stories\badlands\se1\mws_se1_01\mws_se1_01.questphase` / h14 / 73 -> 84 -> 75 |
| `1a50a097cca39ee06949` | 1 | `base\open_world\mini_world_stories\badlands\se1\mws_se1_01\mws_se1_01.questphase` / h14 / 90 -> 91 -> 93 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
