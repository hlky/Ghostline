# ep1-sa-ep1-109

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_109\sa_ep1_109.questphase` | content candidate | 2 / 0 | ep1\openworld\sandbox_activities\courier_spot\sa_ep1_109\scenes\sa_ep1_109_vehicle_enter.scene |
| `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_109\sa_ep1_109_combat_community.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_109\scenes\sa_ep1_109_vehicle_enter.scene` | content candidate | 0 / 4 |  |

## Journal paths observed in these resources

- `ep1/points_of_interest/sandbox_activities/sa_ep1_7`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 1 |
| `questCutControlNodeDefinition` | 3 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 13 |
| `questInputNodeDefinition` | 3 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 3 |
| `questLogicalAndNodeDefinition` | 1 |
| `questLogicalHubNodeDefinition` | 2 |
| `questOutputNodeDefinition` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 3 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 4 |
| `questPauseConditionNodeDefinition[questProximityProgressBar_ConditionType,questUICondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPhaseNodeDefinition` | 1 |
| `questRandomizerNodeDefinition` | 1 |
| `questRenderFxManagerNodeDefinition[questSetFadeInOut_NodeType]` | 2 |
| `questSceneNodeDefinition[scnWorldMarker]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 6 |
| `questTimeManagerNodeDefinition[questShiftTime_NodeType]` | 1 |
| `questUIManagerNodeDefinition[questProximityProgressBar_NodeType]` | 3 |
| `questUIManagerNodeDefinition[questSetHUDEntryForcedVisibility_NodeType]` | 1 |
| `questUIManagerNodeDefinition[questShowOnscreen_NodeType]` | 1 |
| `questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]` | 11 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 5 |
| `questVehicleNodeDefinition[questSetImmovable_NodeType]` | 3 |
| `questVehicleNodeDefinition[questStopVehicle_NodeType]` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 3 |
| `questVehicleNodeDefinition[questToggleForceBrake_NodeType]` | 2 |
| `scnChoiceNode[scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnEndNode[scnNodeId]` | 2 |
| `scnStartNode[scnNodeId]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `beb0324add70d3ab4316` | 11 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_109\sa_ep1_109.questphase` / h16 / 138 -> 160 -> 151 |
| `1e8cc54bddd933feb9f8` | 10 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_109\sa_ep1_109.questphase` / h16 / 163 -> 151 -> 152 |
| `b945f763db731c36815f` | 10 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_109\sa_ep1_109.questphase` / h16 / 160 -> 151 -> 152 |
| `9af8a87f20a910659fa8` | 4 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_109\sa_ep1_109.questphase` / h0 / 15 -> 13 -> 25 |
| `2e1ee5a1324dbeeb9071` | 3 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_109\sa_ep1_109.questphase` / h0 / 43 -> 42 -> 26 |
| `7881fbadf67ef1ff5c0d` | 3 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_109\sa_ep1_109.questphase` / h0 / 6 -> 12 -> 1 |
| `35fc9c9ed3035dd850a8` | 2 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_109\sa_ep1_109.questphase` / h16 / 180 -> 182 -> 177 |
| `3fecf5d780775a6f2a61` | 2 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_109\sa_ep1_109.questphase` / h16 / 140 -> 138 -> 141 |
| `79c8f27b448823241f2e` | 2 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_109\sa_ep1_109.questphase` / h16 / 179 -> 180 -> 182 |
| `827cf5a0b3e00306bbae` | 2 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_109\sa_ep1_109.questphase` / h16 / 137 -> 138 -> 141 |
| `eee7038f799c16b82625` | 2 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_109\sa_ep1_109.questphase` / h16 / 138 -> 179 -> 180 |
| `0f913a040d71afd7e3fc` | 1 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_109\sa_ep1_109.questphase` / h16 / 127 -> 128 -> 136 |
| `10de5d2a81ab97879de5` | 1 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_109\sa_ep1_109.questphase` / h0 / 9 -> 12 -> 1 |
| `1760abb46e61bc4b12dd` | 1 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_109\sa_ep1_109.questphase` / h16 / 140 -> 138 -> 145 |
| `178360ac35259ce804ee` | 1 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_109\sa_ep1_109.questphase` / h0 / 0 -> 44 -> 43 |
| `22ab8bffd29a18b3cd5f` | 1 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_109\sa_ep1_109.questphase` / h16 / 174 -> 153 -> 154 |
| `23b15dfa6e56f7ea2961` | 1 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_109\sa_ep1_109.questphase` / h0 / 5 -> 6 -> 12 |
| `24749f51bf4b51477142` | 1 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_109\sa_ep1_109.questphase` / h0 / 17 -> 18 -> 21 |
| `27572b317e777495ad7e` | 1 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_109\sa_ep1_109.questphase` / h16 / 138 -> 141 -> 142 |
| `2d73eb28337ecf761033` | 1 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_109\sa_ep1_109.questphase` / h0 / 8 -> 9 -> 10 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
