# ep1-mws-cz-03

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\mini_world_stories\combat_zone\mws_cz_03\mws_cz_03.gamedef` | content candidate | 0 / 0 |  |
| `ep1\openworld\mini_world_stories\combat_zone\mws_cz_03\mws_cz_03.quest` | content candidate | 1 / 0 | base\quest\additional_game_elements.questphase; ep1\openworld\ep1_open_world.questphase; ep1\openworld\mini_world_stories\combat_zone\mws_cz_03\mws_cz_03.questphase; ep1\quest\ep1_additional_game_elements.questphase; ep1\quest\test\ep1_chicken_unlocks.questphase |
| `ep1\openworld\mini_world_stories\combat_zone\mws_cz_03\mws_cz_03.questphase` | content candidate | 2 / 0 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questEndNodeDefinition` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 5 |
| `questInputNodeDefinition` | 2 |
| `questOutputNodeDefinition` | 2 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 1 |
| `questPhaseNodeDefinition` | 6 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `07a508d9181a1ec44ac6` | 3 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_03\mws_cz_03.quest` / h0 / 7 -> 6 -> 4 |
| `28040ca8e450266795cd` | 1 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_03\mws_cz_03.questphase` / h0 / 0 -> 15 -> 16 |
| `2c8941c261cff0791c0f` | 1 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_03\mws_cz_03.questphase` / h0 / 13 -> 17 -> 7 |
| `315b5a9439f0b9c6d305` | 1 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_03\mws_cz_03.questphase` / h0 / 14 -> 13 -> 17 |
| `332ec7f7b2263f83bf70` | 1 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_03\mws_cz_03.questphase` / h0 / 16 -> 14 -> 13 |
| `3a3d4ff2ceb6dad82b8e` | 1 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_03\mws_cz_03.quest` / h0 / 0 -> 5 -> 7 |
| `4d34175939e33028cd32` | 1 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_03\mws_cz_03.questphase` / h0 / 15 -> 16 -> 14 |
| `59394a189cb5a316e1d8` | 1 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_03\mws_cz_03.quest` / h0 / 6 -> 4 -> 1 |
| `944b79798f48848a7f9f` | 1 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_03\mws_cz_03.questphase` / h0 / 0 -> 15 -> 14 |
| `9af8a87f20a910659fa8` | 1 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_03\mws_cz_03.quest` / h0 / 5 -> 7 -> 6 |
| `a6273d2f23a9b5aa98c4` | 1 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_03\mws_cz_03.questphase` / h0 / 17 -> 7 -> 1 |
| `af49a3be7d3fce9b8823` | 1 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_03\mws_cz_03.questphase` / h0 / 15 -> 14 -> 13 |
| `b5cee3a20ba9293b67aa` | 1 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_03\mws_cz_03.questphase` / h12 / 0 -> 10 -> 1 |
| `c93c0929afb9e784f4c1` | 1 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_03\mws_cz_03.quest` / h0 / 7 -> 6 -> 11 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
