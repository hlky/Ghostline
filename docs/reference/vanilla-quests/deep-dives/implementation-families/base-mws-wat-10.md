# base-mws-wat-10

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\mini_world_stories\watson\mws_wat_10\mws_wat_10.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\watson\mws_wat_10\mws_wat_10.quest` | content candidate | 1 / 0 | base\open_world\mini_world_stories\watson\mws_wat_10\mws_wat_10.questphase |
| `base\open_world\mini_world_stories\watson\mws_wat_10\mws_wat_10.questphase` | content candidate | 1 / 0 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterStatusEffect_CondtionType]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 2 |
| `questCutControlNodeDefinition` | 2 |
| `questDynamicSpawnSystemNodeDefinition[questDynamicVehicleDespawn_NodeType]` | 1 |
| `questDynamicSpawnSystemNodeDefinition[questDynamicVehicleSpawn_NodeType]` | 1 |
| `questEndNodeDefinition` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 6 |
| `questInputNodeDefinition` | 1 |
| `questLogicalHubNodeDefinition` | 3 |
| `questOutputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition,questLogicalCondition,questRealtimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questTriggerCondition,questVarComparison_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questDistanceCondition,questDynamicSpawnSystemEnemies_ConditionType,questDynamicSpawnSystemEnemyDistance,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questDynamicSpawnSystemCondition,questIsAnyAlive_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questTriggerCondition]` | 2 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 3 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 1 |
| `questPhaseNodeDefinition` | 1 |
| `questStartNodeDefinition` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `1faeb8fb84786fa8bc42` | 3 | `base\open_world\mini_world_stories\watson\mws_wat_10\mws_wat_10.questphase` / h0 / 1 -> 0 -> 2 |
| `4b17b8714a7c6fa254de` | 3 | `base\open_world\mini_world_stories\watson\mws_wat_10\mws_wat_10.questphase` / h0 / 0 -> 2 -> 1 |
| `75fe4a02aeedc5d13dbf` | 3 | `base\open_world\mini_world_stories\watson\mws_wat_10\mws_wat_10.questphase` / h0 / 2 -> 1 -> 0 |
| `983840510260fd329671` | 2 | `base\open_world\mini_world_stories\watson\mws_wat_10\mws_wat_10.questphase` / h0 / 33 -> 34 -> 35 |
| `cf20dd7cab0002cd3442` | 2 | `base\open_world\mini_world_stories\watson\mws_wat_10\mws_wat_10.questphase` / h0 / 36 -> 33 -> 34 |
| `02e67626190f620d1d4d` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_10\mws_wat_10.questphase` / h0 / 42 -> 37 -> 9 |
| `06b0911adbc6c2e11ef5` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_10\mws_wat_10.questphase` / h0 / 42 -> 37 -> 12 |
| `14b68f273226aedf1f92` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_10\mws_wat_10.questphase` / h0 / 15 -> 13 -> 8 |
| `1a36bddda90cacabf744` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_10\mws_wat_10.questphase` / h0 / 38 -> 42 -> 37 |
| `27a0cce617296bee18ef` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_10\mws_wat_10.questphase` / h0 / 8 -> 32 -> 10 |
| `297ab4066b4c3c6f887c` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_10\mws_wat_10.questphase` / h0 / 3 -> 7 -> 14 |
| `2a559fbd2623a467d061` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_10\mws_wat_10.questphase` / h0 / 13 -> 8 -> 32 |
| `2d17e0d42b80ad7ce57b` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_10\mws_wat_10.questphase` / h0 / 21 -> 29 -> 22 |
| `2fef53694f4256108f17` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_10\mws_wat_10.questphase` / h0 / 42 -> 37 -> 13 |
| `3122d8a19f82a37725a4` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_10\mws_wat_10.questphase` / h0 / 37 -> 9 -> 10 |
| `32ae98d08526c5febd65` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_10\mws_wat_10.questphase` / h0 / 37 -> 12 -> 8 |
| `332b1b0497c5763cfa86` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_10\mws_wat_10.questphase` / h0 / 27 -> 28 -> 29 |
| `3abd31e7bfd9b8fa9e87` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_10\mws_wat_10.questphase` / h0 / 8 -> 32 -> 11 |
| `4089bf593ff12fac628b` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_10\mws_wat_10.questphase` / h0 / 12 -> 8 -> 32 |
| `45de337bdb07a91ee3ad` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_10\mws_wat_10.questphase` / h0 / 32 -> 10 -> 11 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
