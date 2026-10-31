# base-sts-wat-kab-106

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_106\community\sts_wat_kab_106_com_enemies.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_106\phases\sts_wat_kab_106.questphase` | content candidate | 1 / 0 | base\open_world\street_stories\watson\kabuki\sts_wat_kab_106\phases\sts_wat_kab_106_combat.questphase; base\open_world\street_stories\watson\kabuki\sts_wat_kab_106\phases\sts_wat_kab_106_streetstories.questphase |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_106\phases\sts_wat_kab_106_combat.questphase` | content candidate | 13 / 0 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_106\phases\sts_wat_kab_106_streetstories.questphase` | content candidate | 6 / 0 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_106\sts_wat_kab_106_gamedef.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_106\sts_wat_kab_106_quest.quest` | content candidate | 1 / 0 | base\open_world\street_stories\watson\kabuki\sts_wat_kab_106\phases\sts_wat_kab_106.questphase |

## Journal paths observed in these resources

- `contacts/regina_jones/sts_wat_kab_106_brief`
- `quests/street_stories/watson/kabuki/sts_wat_kab_106`
- `quests/street_stories/watson/kabuki/sts_wat_kab_106/sts_wat_kab_106/dont_rise_alarm`
- `quests/street_stories/watson/kabuki/sts_wat_kab_106/sts_wat_kab_106/go_to_ho_oh`
- `quests/street_stories/watson/kabuki/sts_wat_kab_106/sts_wat_kab_106/leave_area`
- `quests/street_stories/watson/kabuki/sts_wat_kab_106/sts_wat_kab_106/steal_camera_recording`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 2 |
| `questCombatNodeDefinition[questCombatNodeParams_RestrictMovementToArea]` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 2 |
| `questCutControlNodeDefinition` | 1 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 8 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 2 |
| `questInputNodeDefinition` | 20 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 10 |
| `questLogicalAndNodeDefinition` | 2 |
| `questLogicalXorNodeDefinition` | 1 |
| `questMiscAICommandNode` | 4 |
| `questOutputNodeDefinition` | 10 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 8 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questPhaseNodeDefinition` | 20 |
| `questPhoneManagerNodeDefinition[questOpenMessage_NodeType]` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 2 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 5 |
| `questSpawnManagerNodeDefinition[questLegacy_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 1 |
| `questStartNodeDefinition` | 1 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 4 |
| `questVehicleNodeDefinition[questMoveOnSpline_NodeType]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `987122e5e2fcd167cf6c` | 5 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_106\phases\sts_wat_kab_106_combat.questphase` / h7 / 0 -> 2 -> 3 |
| `d4eed81f829edcc1a916` | 5 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_106\phases\sts_wat_kab_106.questphase` / h0 / 0 -> 2 -> 10 |
| `057faf6705431d5dcd46` | 2 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_106\phases\sts_wat_kab_106_combat.questphase` / h151 / 6 -> 10 -> 12 |
| `138cff49923a75e07348` | 2 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_106\phases\sts_wat_kab_106_streetstories.questphase` / h116 / 3 -> 4 -> 5 |
| `2f0eea9ff31e1b057178` | 2 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_106\phases\sts_wat_kab_106.questphase` / h0 / 2 -> 6 -> 4 |
| `35fc9c9ed3035dd850a8` | 2 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_106\phases\sts_wat_kab_106_combat.questphase` / h151 / 14 -> 16 -> 19 |
| `4ad32694e3b236ba549f` | 2 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_106\phases\sts_wat_kab_106_streetstories.questphase` / h116 / 12 -> 13 -> 14 |
| `bcf9aea1e557153a79d9` | 2 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_106\phases\sts_wat_kab_106_combat.questphase` / h151 / 24 -> 14 -> 16 |
| `d75b2945a59fae639e5c` | 2 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_106\phases\sts_wat_kab_106_combat.questphase` / h151 / 23 -> 24 -> 14 |
| `e2bade3c4563ee7c53cd` | 2 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_106\phases\sts_wat_kab_106_combat.questphase` / h151 / 5 -> 6 -> 8 |
| `e320fbc5b54ace160da5` | 2 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_106\phases\sts_wat_kab_106_streetstories.questphase` / h12 / 0 -> 2 -> 3 |
| `045316bbf4dc2ccf8aca` | 1 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_106\phases\sts_wat_kab_106_combat.questphase` / h151 / 10 -> 12 -> 13 |
| `0de4f0f3a61a46ff6cf2` | 1 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_106\phases\sts_wat_kab_106_streetstories.questphase` / h116 / 9 -> 10 -> 16 |
| `0e55e762d8ff58e5ae49` | 1 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_106\phases\sts_wat_kab_106_combat.questphase` / h151 / 3 -> 4 -> 5 |
| `146d03d186468f0e231d` | 1 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_106\phases\sts_wat_kab_106_combat.questphase` / h151 / 8 -> 11 -> 13 |
| `154238648464beab8298` | 1 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_106\phases\sts_wat_kab_106_combat.questphase` / h151 / 11 -> 13 -> 23 |
| `1618d8c3e60a5672fe4f` | 1 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_106\phases\sts_wat_kab_106_streetstories.questphase` / h116 / 23 -> 3 -> 4 |
| `1666d7526b9bab74f2e2` | 1 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_106\phases\sts_wat_kab_106_streetstories.questphase` / h116 / 5 -> 6 -> 7 |
| `1a9b8893087e174a603f` | 1 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_106\phases\sts_wat_kab_106_streetstories.questphase` / h116 / 6 -> 7 -> 8 |
| `235ed1f97cea566186b0` | 1 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_106\phases\sts_wat_kab_106_streetstories.questphase` / h116 / 7 -> 8 -> 9 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
