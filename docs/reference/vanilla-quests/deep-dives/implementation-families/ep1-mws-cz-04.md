# ep1-mws-cz-04

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\mini_world_stories\combat_zone\mws_cz_04\community\mws_cz_04_community.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\mini_world_stories\combat_zone\mws_cz_04\mws_cz_04.gamedef` | content candidate | 0 / 0 |  |
| `ep1\openworld\mini_world_stories\combat_zone\mws_cz_04\mws_cz_04.quest` | content candidate | 1 / 0 | ep1\openworld\mini_world_stories\combat_zone\mws_cz_04\mws_cz_04.questphase |
| `ep1\openworld\mini_world_stories\combat_zone\mws_cz_04\mws_cz_04.questphase` | content candidate | 5 / 0 | ep1\openworld\mini_world_stories\combat_zone\mws_cz_04\scene\mws_cz_04.scene |
| `ep1\openworld\mini_world_stories\combat_zone\mws_cz_04\scene\mws_cz_04.scene` | content candidate | 0 / 40 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_Kill,questCharacterManagerCombat_NodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetReactionPreset,questReactionPresetRecordSelector]` | 1 |
| `questCombatNodeDefinition` | 2 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 10 |
| `questConditionNodeDefinition[questTimeCondition,questTimePeriod_ConditionType]` | 1 |
| `questEndNodeDefinition` | 1 |
| `questFXManagerNodeDefinition[questPlayFX_NodeType,questPlayFX_NodeTypeParams]` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 6 |
| `questInputNodeDefinition` | 6 |
| `questLogicalAndNodeDefinition` | 3 |
| `questLogicalHubNodeDefinition` | 2 |
| `questLogicalXorNodeDefinition` | 1 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 3 |
| `questOutputNodeDefinition` | 7 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHealth_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 4 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questTriggerCondition,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 2 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 3 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 2 |
| `questSceneNodeDefinition[scnWorldMarker]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 16 |
| `questStartNodeDefinition` | 1 |
| `questUIManagerNodeDefinition[questProgressBar_NodeType]` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 4 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 2 |
| `questVoicesetManagerNodeDefinition[questChangeVoicesetState_NodeType,questChangeVoicesetState_NodeTypeParams]` | 1 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 4 |
| `scnAndNode[scnNodeId]` | 1 |
| `scnChoiceNode[questBuild_ConditionType,questStatsCondition,questUniversalRef,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnEndNode[scnNodeId]` | 2 |
| `scnHubNode[scnNodeId]` | 4 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 2 |
| `scnStartNode[scnNodeId]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `29607172ea9d2371e148` | 8 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_04\mws_cz_04.questphase` / h42 / 16 -> 11 -> 2 |
| `9b1546642b468405d31d` | 5 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_04\mws_cz_04.questphase` / h42 / 11 -> 2 -> 6 |
| `ff3c99d0d23a6a421302` | 5 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_04\mws_cz_04.questphase` / h42 / 11 -> 12 -> 9 |
| `2251a3c44ea8a153bc79` | 4 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_04\mws_cz_04.questphase` / h318 / 0 -> 8 -> 3 |
| `e1c81aaffe3700aa8a08` | 4 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_04\mws_cz_04.questphase` / h42 / 16 -> 11 -> 15 |
| `74173965f3210990c9fe` | 3 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_04\scene\mws_cz_04.scene` / scene / 141 -> 197 -> 97 |
| `a9f75d78d6ca065ee67d` | 3 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_04\scene\mws_cz_04.scene` / scene / 197 -> 100 -> 119 |
| `3fa1208cc0da990e02e2` | 2 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_04\mws_cz_04.questphase` / h190 / 14 -> 5 -> 4 |
| `433b30c57bbf90bfb64b` | 2 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_04\mws_cz_04.questphase` / h42 / 5 -> 9 -> 10 |
| `55bd509a3f9e32bd1d36` | 2 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_04\mws_cz_04.questphase` / h42 / 2 -> 6 -> 19 |
| `5bdc8c8f239d1d258b0f` | 2 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_04\mws_cz_04.questphase` / h190 / 11 -> 14 -> 5 |
| `67c23d9a6d194d22eb0f` | 2 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_04\mws_cz_04.questphase` / h190 / 13 -> 14 -> 5 |
| `8e1d2b6d16b0384b26b3` | 2 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_04\mws_cz_04.questphase` / h42 / 3 -> 7 -> 10 |
| `b7bc8d9b93db78f94b79` | 2 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_04\mws_cz_04.questphase` / h42 / 4 -> 8 -> 10 |
| `ee1368560de3dd07b894` | 2 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_04\mws_cz_04.questphase` / h190 / 12 -> 14 -> 5 |
| `013760bef05de7255ccc` | 1 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_04\mws_cz_04.questphase` / h28 / 7 -> 2 -> 3 |
| `03bde6ef1888ecd357fd` | 1 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_04\mws_cz_04.questphase` / h190 / 3 -> 18 -> 6 |
| `05f0e7f619845b41a541` | 1 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_04\scene\mws_cz_04.scene` / scene / 30 -> 172 -> 127 |
| `19665e3783f6f51a7337` | 1 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_04\scene\mws_cz_04.scene` / scene / 1 -> 61 -> 70 |
| `21100aec4757412cdd42` | 1 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_04\mws_cz_04.questphase` / h28 / 0 -> 2 -> 3 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
