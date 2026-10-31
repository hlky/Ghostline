# base-mws-wat-04

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\mini_world_stories\watson\mws_wat_04\community\mws_wat_04.community` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\watson\mws_wat_04\mws_wat_04.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\watson\mws_wat_04\mws_wat_04.quest` | content candidate | 1 / 0 | base\open_world\mini_world_stories\watson\mws_wat_04\mws_wat_04.questphase |
| `base\open_world\mini_world_stories\watson\mws_wat_04\mws_wat_04.questphase` | content candidate | 2 / 0 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetReactionPreset,questReactionPresetRecordSelector]` | 1 |
| `questCombatNodeDefinition` | 1 |
| `questConditionNodeDefinition[questTriggerCondition]` | 1 |
| `questCutControlNodeDefinition` | 1 |
| `questDeletionMarkerNodeDefinition` | 1 |
| `questEndNodeDefinition` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 2 |
| `questInputNodeDefinition` | 4 |
| `questLogicalHubNodeDefinition` | 3 |
| `questLogicalXorNodeDefinition` | 2 |
| `questOutputNodeDefinition` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questTriggerCondition,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 5 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 1 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questRandomizerNodeDefinition` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questSwitchNodeDefinition[questConditionItem,questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questUIManagerNodeDefinition[questDisplayMessageBox_NodeType]` | 1 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 2 |
| `questVehicleNodeDefinition[questSetImmovable_NodeType]` | 2 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 2 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 3 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 4 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `e67e2c0c37da710254f3` | 4 | `base\open_world\mini_world_stories\watson\mws_wat_04\mws_wat_04.questphase` / h18 / 103 -> 106 -> 9 |
| `0233230442df581e2fd7` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_04\mws_wat_04.questphase` / h18 / 107 -> 111 -> 39 |
| `056f65b5401e52f37bc4` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_04\mws_wat_04.questphase` / h18 / 23 -> 22 -> 110 |
| `05b55b664997ab6e079f` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_04\mws_wat_04.questphase` / h18 / 106 -> 75 -> 76 |
| `05fb15bd4551094b663b` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_04\mws_wat_04.questphase` / h18 / 71 -> 75 -> 76 |
| `072241491beaf6604a7b` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_04\mws_wat_04.questphase` / h18 / 5 -> 9 -> 17 |
| `1a50a097cca39ee06949` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_04\mws_wat_04.questphase` / h18 / 96 -> 4 -> 77 |
| `236ed03ec18a1ea92e6c` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_04\mws_wat_04.questphase` / h18 / 74 -> 71 -> 73 |
| `288f699c94465cec5d3f` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_04\mws_wat_04.questphase` / h18 / 106 -> 73 -> 76 |
| `333fc369e220cb8296a1` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_04\mws_wat_04.questphase` / h18 / 106 -> 108 -> 105 |
| `38ba89bc8ecd473c8dc7` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_04\mws_wat_04.questphase` / h18 / 6 -> 96 -> 4 |
| `51e9487677c4966c2b10` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_04\mws_wat_04.questphase` / h18 / 103 -> 106 -> 108 |
| `62a059f79a056707bacf` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_04\mws_wat_04.questphase` / h18 / 76 -> 5 -> 9 |
| `6791cbbe6b26cff8e34a` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_04\mws_wat_04.questphase` / h18 / 4 -> 107 -> 111 |
| `67a344dbc2ecf5a65da5` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_04\mws_wat_04.questphase` / h18 / 9 -> 17 -> 60 |
| `68708e584f27e857dcd1` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_04\mws_wat_04.questphase` / h18 / 106 -> 5 -> 9 |
| `6b3fa310c97b28404a88` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_04\mws_wat_04.questphase` / h18 / 9 -> 17 -> 18 |
| `6c9ebe113ef18530f07e` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_04\mws_wat_04.questphase` / h18 / 17 -> 18 -> 5 |
| `70f4d7c3ea837ffbf963` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_04\mws_wat_04.questphase` / h18 / 103 -> 106 -> 5 |
| `71892f49b88f7b8bb8be` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_04\mws_wat_04.questphase` / h18 / 2 -> 6 -> 96 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
