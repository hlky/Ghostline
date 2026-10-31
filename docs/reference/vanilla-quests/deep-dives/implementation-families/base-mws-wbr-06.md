# base-mws-wbr-06

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\mini_world_stories\westbrook\mws_wbr_06\mws_wbr_06.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\westbrook\mws_wbr_06\mws_wbr_06.quest` | content candidate | 1 / 0 | base\open_world\mini_world_stories\westbrook\mws_wbr_06\mws_wbr_06.questphase |
| `base\open_world\mini_world_stories\westbrook\mws_wbr_06\mws_wbr_06.questphase` | content candidate | 1 / 0 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 2 |
| `questCutControlNodeDefinition` | 2 |
| `questDynamicSpawnSystemNodeDefinition[questDynamicVehicleDespawn_NodeType]` | 1 |
| `questDynamicSpawnSystemNodeDefinition[questDynamicVehicleSpawn_NodeType]` | 1 |
| `questEndNodeDefinition` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 3 |
| `questInputNodeDefinition` | 1 |
| `questLogicalHubNodeDefinition` | 2 |
| `questOutputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition,questLogicalCondition,questRealtimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questTriggerCondition,questVarComparison_ConditionType]` | 1 |
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
| `983840510260fd329671` | 2 | `base\open_world\mini_world_stories\westbrook\mws_wbr_06\mws_wbr_06.questphase` / h0 / 30 -> 31 -> 32 |
| `cf20dd7cab0002cd3442` | 2 | `base\open_world\mini_world_stories\westbrook\mws_wbr_06\mws_wbr_06.questphase` / h0 / 33 -> 30 -> 31 |
| `06126cee8f6cfda2b56e` | 1 | `base\open_world\mini_world_stories\westbrook\mws_wbr_06\mws_wbr_06.questphase` / h0 / 16 -> 17 -> 35 |
| `0d57c84444cbe4eecffb` | 1 | `base\open_world\mini_world_stories\westbrook\mws_wbr_06\mws_wbr_06.questphase` / h0 / 35 -> 34 -> 15 |
| `14b68f273226aedf1f92` | 1 | `base\open_world\mini_world_stories\westbrook\mws_wbr_06\mws_wbr_06.questphase` / h0 / 17 -> 15 -> 10 |
| `1faeb8fb84786fa8bc42` | 1 | `base\open_world\mini_world_stories\westbrook\mws_wbr_06\mws_wbr_06.questphase` / h0 / 3 -> 2 -> 4 |
| `27a0cce617296bee18ef` | 1 | `base\open_world\mini_world_stories\westbrook\mws_wbr_06\mws_wbr_06.questphase` / h0 / 10 -> 28 -> 12 |
| `297ab4066b4c3c6f887c` | 1 | `base\open_world\mini_world_stories\westbrook\mws_wbr_06\mws_wbr_06.questphase` / h0 / 5 -> 9 -> 16 |
| `2a559fbd2623a467d061` | 1 | `base\open_world\mini_world_stories\westbrook\mws_wbr_06\mws_wbr_06.questphase` / h0 / 15 -> 10 -> 28 |
| `2c8817019d7f71d7315b` | 1 | `base\open_world\mini_world_stories\westbrook\mws_wbr_06\mws_wbr_06.questphase` / h0 / 35 -> 34 -> 14 |
| `2d17e0d42b80ad7ce57b` | 1 | `base\open_world\mini_world_stories\westbrook\mws_wbr_06\mws_wbr_06.questphase` / h0 / 0 -> 25 -> 1 |
| `3122d8a19f82a37725a4` | 1 | `base\open_world\mini_world_stories\westbrook\mws_wbr_06\mws_wbr_06.questphase` / h0 / 34 -> 11 -> 12 |
| `32ae98d08526c5febd65` | 1 | `base\open_world\mini_world_stories\westbrook\mws_wbr_06\mws_wbr_06.questphase` / h0 / 34 -> 14 -> 10 |
| `32d75101169dc16f0217` | 1 | `base\open_world\mini_world_stories\westbrook\mws_wbr_06\mws_wbr_06.questphase` / h0 / 28 -> 22 -> 23 |
| `332b1b0497c5763cfa86` | 1 | `base\open_world\mini_world_stories\westbrook\mws_wbr_06\mws_wbr_06.questphase` / h0 / 23 -> 24 -> 25 |
| `3abd31e7bfd9b8fa9e87` | 1 | `base\open_world\mini_world_stories\westbrook\mws_wbr_06\mws_wbr_06.questphase` / h0 / 10 -> 28 -> 13 |
| `4089bf593ff12fac628b` | 1 | `base\open_world\mini_world_stories\westbrook\mws_wbr_06\mws_wbr_06.questphase` / h0 / 14 -> 10 -> 28 |
| `45de337bdb07a91ee3ad` | 1 | `base\open_world\mini_world_stories\westbrook\mws_wbr_06\mws_wbr_06.questphase` / h0 / 28 -> 12 -> 13 |
| `480bdd302dd063e0da14` | 1 | `base\open_world\mini_world_stories\westbrook\mws_wbr_06\mws_wbr_06.questphase` / h0 / 0 -> 30 -> 31 |
| `4b17b8714a7c6fa254de` | 1 | `base\open_world\mini_world_stories\westbrook\mws_wbr_06\mws_wbr_06.questphase` / h0 / 2 -> 4 -> 3 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
