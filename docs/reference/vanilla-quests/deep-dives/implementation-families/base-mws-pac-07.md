# base-mws-pac-07

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\mini_world_stories\pacifica\mws_pac_07\mws_pac_07.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\pacifica\mws_pac_07\mws_pac_07.quest` | content candidate | 1 / 0 | base\open_world\mini_world_stories\pacifica\mws_pac_07\mws_pac_07.questphase |
| `base\open_world\mini_world_stories\pacifica\mws_pac_07\mws_pac_07.questphase` | content candidate | 1 / 0 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 3 |
| `questCutControlNodeDefinition` | 2 |
| `questDynamicSpawnSystemNodeDefinition[questDynamicVehicleDespawn_NodeType]` | 1 |
| `questDynamicSpawnSystemNodeDefinition[questDynamicVehicleSpawn_NodeType]` | 1 |
| `questEndNodeDefinition` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 6 |
| `questInputNodeDefinition` | 1 |
| `questLogicalHubNodeDefinition` | 4 |
| `questOutputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition,questLogicalCondition,questRealtimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questTriggerCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceCondition,questDynamicSpawnSystemEnemies_ConditionType,questDynamicSpawnSystemEnemyDistance,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questDynamicSpawnSystemCondition,questIsAnyAlive_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questTriggerCondition]` | 2 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 3 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 1 |
| `questPhaseNodeDefinition` | 1 |
| `questStartNodeDefinition` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `983840510260fd329671` | 2 | `base\open_world\mini_world_stories\pacifica\mws_pac_07\mws_pac_07.questphase` / h0 / 31 -> 32 -> 33 |
| `cf20dd7cab0002cd3442` | 2 | `base\open_world\mini_world_stories\pacifica\mws_pac_07\mws_pac_07.questphase` / h0 / 34 -> 31 -> 32 |
| `02e67626190f620d1d4d` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_07\mws_pac_07.questphase` / h0 / 40 -> 35 -> 9 |
| `06126cee8f6cfda2b56e` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_07\mws_pac_07.questphase` / h0 / 14 -> 15 -> 36 |
| `06b0911adbc6c2e11ef5` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_07\mws_pac_07.questphase` / h0 / 40 -> 35 -> 12 |
| `14b68f273226aedf1f92` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_07\mws_pac_07.questphase` / h0 / 15 -> 13 -> 8 |
| `1a36bddda90cacabf744` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_07\mws_pac_07.questphase` / h0 / 36 -> 40 -> 35 |
| `1faeb8fb84786fa8bc42` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_07\mws_pac_07.questphase` / h0 / 1 -> 0 -> 2 |
| `27a0cce617296bee18ef` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_07\mws_pac_07.questphase` / h0 / 8 -> 30 -> 10 |
| `297ab4066b4c3c6f887c` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_07\mws_pac_07.questphase` / h0 / 3 -> 7 -> 14 |
| `2a559fbd2623a467d061` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_07\mws_pac_07.questphase` / h0 / 13 -> 8 -> 30 |
| `2e04a620886c7d6307a9` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_07\mws_pac_07.questphase` / h0 / 26 -> 27 -> 24 |
| `2fef53694f4256108f17` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_07\mws_pac_07.questphase` / h0 / 40 -> 35 -> 13 |
| `3122d8a19f82a37725a4` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_07\mws_pac_07.questphase` / h0 / 35 -> 9 -> 10 |
| `32ae98d08526c5febd65` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_07\mws_pac_07.questphase` / h0 / 35 -> 12 -> 8 |
| `332b1b0497c5763cfa86` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_07\mws_pac_07.questphase` / h0 / 22 -> 23 -> 24 |
| `3abd31e7bfd9b8fa9e87` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_07\mws_pac_07.questphase` / h0 / 8 -> 30 -> 11 |
| `4089bf593ff12fac628b` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_07\mws_pac_07.questphase` / h0 / 12 -> 8 -> 30 |
| `45de337bdb07a91ee3ad` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_07\mws_pac_07.questphase` / h0 / 30 -> 10 -> 11 |
| `480bdd302dd063e0da14` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_07\mws_pac_07.questphase` / h0 / 19 -> 31 -> 32 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
