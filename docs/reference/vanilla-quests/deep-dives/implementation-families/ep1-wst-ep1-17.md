# ep1-wst-ep1-17

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\world_stories\wst_ep1_17\community\wst_ep1_17_enemies.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\world_stories\wst_ep1_17\wst_ep1_17.gamedef` | content candidate | 0 / 0 |  |
| `ep1\openworld\world_stories\wst_ep1_17\wst_ep1_17.quest` | content candidate | 1 / 0 | ep1\openworld\world_stories\wst_ep1_17\wst_ep1_17.questphase |
| `ep1\openworld\world_stories\wst_ep1_17\wst_ep1_17.questphase` | content candidate | 4 / 0 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 1 |
| `questCutControlNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 2 |
| `questInputNodeDefinition` | 6 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questLogicalHubNodeDefinition` | 2 |
| `questLogicalXorNodeDefinition` | 3 |
| `questOutputNodeDefinition` | 5 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 6 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 3 |
| `questPauseConditionNodeDefinition[questTickDelay_ConditionType,questTimeCondition]` | 3 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 1 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 3 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 4 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 3 |
| `questStartNodeDefinition` | 1 |
| `questVehicleNodeDefinition[questSetImmovable_NodeType]` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 2 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 17 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `bfe95df47bd1ca67330f` | 11 | `ep1\openworld\world_stories\wst_ep1_17\wst_ep1_17.questphase` / h9 / 19 -> 20 -> 21 |
| `e0b4366c76fe767c457b` | 3 | `ep1\openworld\world_stories\wst_ep1_17\wst_ep1_17.questphase` / h182 / 3 -> 6 -> 13 |
| `44001c669afc743ed647` | 2 | `ep1\openworld\world_stories\wst_ep1_17\wst_ep1_17.questphase` / h9 / 12 -> 19 -> 20 |
| `736e12da56db0f348c65` | 2 | `ep1\openworld\world_stories\wst_ep1_17\wst_ep1_17.questphase` / h9 / 5 -> 12 -> 19 |
| `016e710128e3126421d3` | 1 | `ep1\openworld\world_stories\wst_ep1_17\wst_ep1_17.questphase` / h182 / 34 -> 31 -> 63 |
| `01cc762cd06f16743b1c` | 1 | `ep1\openworld\world_stories\wst_ep1_17\wst_ep1_17.questphase` / h9 / 22 -> 23 -> 1 |
| `09b4186cee6a735809ee` | 1 | `ep1\openworld\world_stories\wst_ep1_17\wst_ep1_17.questphase` / h0 / 43 -> 38 -> 42 |
| `0c2eb007722f3d441878` | 1 | `ep1\openworld\world_stories\wst_ep1_17\wst_ep1_17.questphase` / h182 / 25 -> 30 -> 53 |
| `2ed7a8c4ef68d2f35129` | 1 | `ep1\openworld\world_stories\wst_ep1_17\wst_ep1_17.questphase` / h103 / 0 -> 17 -> 4 |
| `35423f3d37f4af7dea78` | 1 | `ep1\openworld\world_stories\wst_ep1_17\wst_ep1_17.questphase` / h182 / 31 -> 63 -> 65 |
| `3df44c2e05455d8969e0` | 1 | `ep1\openworld\world_stories\wst_ep1_17\wst_ep1_17.questphase` / h182 / 64 -> 3 -> 40 |
| `41cea177d8258d26398f` | 1 | `ep1\openworld\world_stories\wst_ep1_17\wst_ep1_17.questphase` / h9 / 0 -> 3 -> 16 |
| `43eba6d85cda69b66517` | 1 | `ep1\openworld\world_stories\wst_ep1_17\wst_ep1_17.questphase` / h182 / 23 -> 22 -> 21 |
| `484ddec78bd3015739fd` | 1 | `ep1\openworld\world_stories\wst_ep1_17\wst_ep1_17.questphase` / h182 / 62 -> 42 -> 64 |
| `4db18aaae4b08d077f4e` | 1 | `ep1\openworld\world_stories\wst_ep1_17\wst_ep1_17.questphase` / h9 / 4 -> 5 -> 12 |
| `6e3b35557bcc40a5d957` | 1 | `ep1\openworld\world_stories\wst_ep1_17\wst_ep1_17.questphase` / h182 / 3 -> 8 -> 9 |
| `6e9d673e1e846e4cff4c` | 1 | `ep1\openworld\world_stories\wst_ep1_17\wst_ep1_17.questphase` / h9 / 21 -> 22 -> 23 |
| `717c4c30094e81e3c792` | 1 | `ep1\openworld\world_stories\wst_ep1_17\wst_ep1_17.questphase` / h182 / 42 -> 64 -> 3 |
| `75582ae0b4c1620a124c` | 1 | `ep1\openworld\world_stories\wst_ep1_17\wst_ep1_17.questphase` / h103 / 15 -> 16 -> 1 |
| `7758ba42efaa96804ff3` | 1 | `ep1\openworld\world_stories\wst_ep1_17\wst_ep1_17.questphase` / h182 / 23 -> 20 -> 21 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
