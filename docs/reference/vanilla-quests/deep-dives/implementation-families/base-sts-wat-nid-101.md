# base-sts-wat-nid-101

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_101\community\sts_wat_nid_101_maelstrom.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_101\phases\sts_wat_nid_101_combat.questphase` | content candidate | 6 / 0 |  |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_101\phases\sts_wat_nid_101_ow.questphase` | content candidate | 4 / 0 |  |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_101\phases\sts_wat_nid_101_phase.questphase` | content candidate | 1 / 0 | base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_101\phases\sts_wat_nid_101_combat.questphase; base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_101\phases\sts_wat_nid_101_ow.questphase |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_101\sts_wat_nid_101.quest` | content candidate | 1 / 0 | base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_101\phases\sts_wat_nid_101_phase.questphase |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_101\sts_wat_nid_101_nc_def.gamedef` | content candidate | 0 / 0 |  |

## Journal paths observed in these resources

- `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_101`
- `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_101/sts_wat_nid_101/acquire_data`
- `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_101/sts_wat_nid_101/drop_point`
- `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_101/sts_wat_nid_101/reach_area`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questEndNodeDefinition` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 2 |
| `questInputNodeDefinition` | 11 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 8 |
| `questLogicalAndNodeDefinition` | 1 |
| `questMiscAICommandNode` | 1 |
| `questOutputNodeDefinition` | 7 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 2 |
| `questPhaseNodeDefinition` | 11 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 1 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 1 |
| `questStartNodeDefinition` | 1 |
| `questUIManagerNodeDefinition[questDisplayMessageBox_NodeType]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `138cff49923a75e07348` | 2 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_101\phases\sts_wat_nid_101_ow.questphase` / h33 / 3 -> 9 -> 4 |
| `1618d8c3e60a5672fe4f` | 1 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_101\phases\sts_wat_nid_101_ow.questphase` / h33 / 15 -> 16 -> 9 |
| `252df7af803a768953df` | 1 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_101\phases\sts_wat_nid_101_ow.questphase` / h33 / 7 -> 12 -> 8 |
| `2f0eea9ff31e1b057178` | 1 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_101\phases\sts_wat_nid_101_phase.questphase` / h0 / 4 -> 5 -> 3 |
| `400e13c61734c26e268c` | 1 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_101\phases\sts_wat_nid_101_ow.questphase` / h12 / 0 -> 2 -> 1 |
| `4803de0710dd8d0fcd3d` | 1 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_101\phases\sts_wat_nid_101_ow.questphase` / h33 / 5 -> 11 -> 6 |
| `4e9253a72e6b0134b8dd` | 1 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_101\phases\sts_wat_nid_101_ow.questphase` / h33 / 9 -> 4 -> 5 |
| `4f64918875c7d975bed8` | 1 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_101\phases\sts_wat_nid_101_ow.questphase` / h33 / 4 -> 5 -> 11 |
| `59394a189cb5a316e1d8` | 1 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_101\sts_wat_nid_101.quest` / h0 / 3 -> 2 -> 1 |
| `647ea9ce31c01a3e6527` | 1 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_101\phases\sts_wat_nid_101_phase.questphase` / h0 / 0 -> 4 -> 2 |
| `689f668010ea299e6eb0` | 1 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_101\phases\sts_wat_nid_101_combat.questphase` / h86 / 0 -> 4 -> 2 |
| `72456e8dd927fd679172` | 1 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_101\phases\sts_wat_nid_101_combat.questphase` / h12 / 2 -> 3 -> 7 |
| `756574daa5e17821e522` | 1 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_101\phases\sts_wat_nid_101_ow.questphase` / h33 / 6 -> 7 -> 12 |
| `808c42396a9735fe3a65` | 1 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_101\phases\sts_wat_nid_101_combat.questphase` / h12 / 0 -> 5 -> 6 |
| `88d3c8c9b598e740b5ea` | 1 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_101\phases\sts_wat_nid_101_phase.questphase` / h0 / 0 -> 4 -> 5 |
| `95d253305075d18f00cc` | 1 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_101\phases\sts_wat_nid_101_ow.questphase` / h33 / 15 -> 3 -> 9 |
| `987122e5e2fcd167cf6c` | 1 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_101\phases\sts_wat_nid_101_combat.questphase` / h12 / 0 -> 2 -> 3 |
| `a307896b77afd6a7b01d` | 1 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_101\phases\sts_wat_nid_101_ow.questphase` / h33 / 12 -> 8 -> 13 |
| `c25631343077baa2819b` | 1 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_101\phases\sts_wat_nid_101_combat.questphase` / h12 / 5 -> 6 -> 7 |
| `c980e30cb2fea99eb440` | 1 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_101\phases\sts_wat_nid_101_combat.questphase` / h12 / 3 -> 7 -> 1 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
