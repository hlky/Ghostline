# base-mws-arr-03

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\mini_world_stories\santo_domingo\mws_arr_03\community\mws_arr_03.community` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\santo_domingo\mws_arr_03\community\mws_arr_03_nacked_run.community` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\santo_domingo\mws_arr_03\mws_arr_03.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\santo_domingo\mws_arr_03\mws_arr_03.quest` | content candidate | 1 / 0 | base\open_world\mini_world_stories\santo_domingo\mws_arr_03\mws_arr_03.questphase |
| `base\open_world\mini_world_stories\santo_domingo\mws_arr_03\mws_arr_03.questphase` | content candidate | 5 / 0 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_Kill,questCharacterManagerCombat_NodeType]` | 3 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetGroupsAttitude]` | 10 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetReactionPreset,questReactionPresetRecordSelector]` | 5 |
| `questCombatNodeDefinition` | 2 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 2 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 3 |
| `questConditionNodeDefinition[questDestruction_ConditionType,questObjectCondition]` | 1 |
| `questConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 7 |
| `questCutControlNodeDefinition` | 8 |
| `questDeletionMarkerNodeDefinition` | 5 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 1 |
| `questFXManagerNodeDefinition[questPlayFX_NodeType,questPlayFX_NodeTypeParams]` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 7 |
| `questInputNodeDefinition` | 8 |
| `questItemManagerNodeDefinition[questAddRemoveItem_NodeType,questAddRemoveItem_NodeTypeParams,questUniversalRef]` | 1 |
| `questLogicalHubNodeDefinition` | 5 |
| `questLogicalXorNodeDefinition` | 6 |
| `questMovePuppetNodeDefinition[questFollowParams,questUniversalRef]` | 1 |
| `questMovePuppetNodeDefinition[questMoveToParams,questUniversalRef]` | 10 |
| `questOutputNodeDefinition` | 5 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition,questFactsDBCondition,questGatherTriggerCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition,questFactsDBCondition,questLogicalCondition,questTriggerCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterStatusEffect_CondtionType]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questTriggerCondition,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 11 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 1 |
| `questPhaseNodeDefinition` | 4 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questPuppetAIManagerNodeDefinition[questPuppetAIManagerNodeDefinitionEntry]` | 3 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 4 |
| `questStartNodeDefinition` | 1 |
| `questUIManagerNodeDefinition[questDisplayMessageBox_NodeType]` | 1 |
| `questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]` | 2 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 7 |
| `questVehicleNodeDefinition[questSetImmovable_NodeType]` | 3 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 1 |
| `questVehicleNodeDefinition[questToggleForceBrake_NodeType]` | 3 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 5 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `6537f5c0734cc114cf7d` | 10 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_03\mws_arr_03.questphase` / h428 / 16 -> 17 -> 3 |
| `97161d2ba073224f206d` | 9 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_03\mws_arr_03.questphase` / h428 / 17 -> 11 -> 12 |
| `a7d97ec012af759a3d2c` | 8 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_03\mws_arr_03.questphase` / h428 / 9 -> 11 -> 12 |
| `56c53a847765e20a971f` | 4 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_03\mws_arr_03.questphase` / h2 / 281 -> 15 -> 14 |
| `8e7134d102afde206bbb` | 4 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_03\mws_arr_03.questphase` / h2 / 99 -> 281 -> 15 |
| `42d456f68cbe3d8345c3` | 3 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_03\mws_arr_03.questphase` / h2 / 14 -> 17 -> 16 |
| `6bade9a6171d604fd6d8` | 3 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_03\mws_arr_03.questphase` / h2 / 281 -> 14 -> 17 |
| `7b44344c01ad5161d3ff` | 3 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_03\mws_arr_03.questphase` / h2 / 15 -> 14 -> 17 |
| `015ec26943ac36b730cc` | 2 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_03\mws_arr_03.questphase` / h2 / 281 -> 124 -> 274 |
| `3dcb4cf54a7e1c5cacd2` | 2 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_03\mws_arr_03.questphase` / h2 / 321 -> 322 -> 320 |
| `4e0f1bf83cd658232343` | 2 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_03\mws_arr_03.questphase` / h2 / 140 -> 104 -> 119 |
| `7d5223f10783a920aec8` | 2 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_03\mws_arr_03.questphase` / h2 / 177 -> 175 -> 23 |
| `7e14a8406d41557d9166` | 2 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_03\mws_arr_03.questphase` / h2 / 323 -> 322 -> 320 |
| `abc85128ec42b5bdc6f6` | 2 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_03\mws_arr_03.questphase` / h428 / 0 -> 14 -> 16 |
| `ae7e255b3abc538a084c` | 2 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_03\mws_arr_03.questphase` / h428 / 0 -> 15 -> 16 |
| `fbf0230174ab2a43ed80` | 2 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_03\mws_arr_03.questphase` / h2 / 118 -> 259 -> 277 |
| `00ba12666cf2a6c1ee5c` | 1 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_03\mws_arr_03.questphase` / h2 / 25 -> 53 -> 158 |
| `14e5501208bf98df9dd1` | 1 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_03\mws_arr_03.questphase` / h2 / 93 -> 333 -> 237 |
| `1bdee0593801bc909107` | 1 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_03\mws_arr_03.questphase` / h2 / 272 -> 90 -> 93 |
| `266efd4da33fd64c3bc6` | 1 | `base\open_world\mini_world_stories\santo_domingo\mws_arr_03\mws_arr_03.questphase` / h2 / 279 -> 282 -> 124 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
