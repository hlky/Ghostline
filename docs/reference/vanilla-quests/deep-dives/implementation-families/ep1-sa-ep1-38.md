# ep1-sa-ep1-38

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\sandbox_activities\sa_ep1_38\community\sa_ep1_38_av_com.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_38\community\sa_ep1_38_com.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_38\community\sa_ep1_38_var_01_com.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_38\community\sa_ep1_38_var_01_reinforcement_com.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_38\community\sa_ep1_38_var_02_com.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_38\sa_ep1_38.gamedef` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_38\sa_ep1_38.quest` | content candidate | 1 / 0 | ep1\openworld\sandbox_activities\sa_ep1_30\scenes\sa_ep1_30_chicken_test.scene; ep1\openworld\sandbox_activities\sa_ep1_38\sa_ep1_38.questphase |
| `ep1\openworld\sandbox_activities\sa_ep1_38\sa_ep1_38.questphase` | content candidate | 7 / 0 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioEventNodeType]` | 12 |
| `questCharacterManagerNodeDefinition[questCharacterManagerVisuals_ChangeEntityAppearance,questCharacterManagerVisuals_EntityAppearanceOperationBaseEntityAppearanceEntry,questCharacterManagerVisuals_NodeType]` | 3 |
| `questCheckpointNodeDefinition` | 3 |
| `questCombatNodeDefinition` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 7 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 6 |
| `questCutControlNodeDefinition` | 3 |
| `questEntityManagerNodeDefinition[questEntityManagerToggleComponent_NodeType,questEntityManagerToggleComponent_NodeTypeParams]` | 4 |
| `questEventManagerNodeDefinition` | 9 |
| `questFXManagerNodeDefinition[questPlayFX_NodeType,questPlayFX_NodeTypeParams]` | 15 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 25 |
| `questInputNodeDefinition` | 10 |
| `questItemManagerNodeDefinition[questReInitContainers_NodeType,questReInitContainers_NodeTypeParams]` | 2 |
| `questLogicalAndNodeDefinition` | 4 |
| `questLogicalHubNodeDefinition` | 3 |
| `questLogicalXorNodeDefinition` | 3 |
| `questMiscAICommandNode` | 8 |
| `questOutputNodeDefinition` | 10 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 10 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 3 |
| `questPauseConditionNodeDefinition[questNodeLoadingCondition]` | 2 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 13 |
| `questPauseConditionNodeDefinition[questTickDelay_ConditionType,questTimeCondition]` | 4 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 16 |
| `questPhaseNodeDefinition` | 7 |
| `questRandomizerNodeDefinition` | 2 |
| `questSceneNodeDefinition[scnWorldMarker]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 33 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 1 |
| `questStartNodeDefinition` | 1 |
| `questSwitchNodeDefinition[questConditionItem,questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questTransformAnimatorNodeDefinition[questTransformAnimatorNode_Action_Play]` | 1 |
| `questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]` | 1 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 8 |
| `questVehicleNodeDefinition[questMoveOnSpline_NodeType]` | 6 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 18 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 8 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `a5f6ff0df46f7043f2b5` | 12 | `ep1\openworld\sandbox_activities\sa_ep1_38\sa_ep1_38.questphase` / h7 / 367 -> 362 -> 363 |
| `27d3d4c401ea569d6469` | 8 | `ep1\openworld\sandbox_activities\sa_ep1_38\sa_ep1_38.questphase` / h7 / 364 -> 343 -> 350 |
| `05c7a2151e0cd17400d5` | 6 | `ep1\openworld\sandbox_activities\sa_ep1_38\sa_ep1_38.questphase` / h271 / 15 -> 27 -> 3 |
| `3e6653e916afcf7cc2e1` | 6 | `ep1\openworld\sandbox_activities\sa_ep1_38\sa_ep1_38.questphase` / h271 / 15 -> 27 -> 21 |
| `fc910f43d5ff9aabecc6` | 6 | `ep1\openworld\sandbox_activities\sa_ep1_38\sa_ep1_38.questphase` / h271 / 2 -> 15 -> 27 |
| `120c5c4bbfcbfae70bc4` | 5 | `ep1\openworld\sandbox_activities\sa_ep1_38\sa_ep1_38.questphase` / h565 / 424 -> 423 -> 425 |
| `8a68d69cd367a28a1a4d` | 4 | `ep1\openworld\sandbox_activities\sa_ep1_38\sa_ep1_38.questphase` / h565 / 434 -> 435 -> 442 |
| `cb15f618f342a00de266` | 4 | `ep1\openworld\sandbox_activities\sa_ep1_38\sa_ep1_38.questphase` / h565 / 439 -> 429 -> 430 |
| `01cc762cd06f16743b1c` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_38\sa_ep1_38.questphase` / h7 / 411 -> 359 -> 330 |
| `0307c8e1c2bd71322d7d` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_38\sa_ep1_38.questphase` / h7 / 392 -> 354 -> 424 |
| `0f6060800f34fba21084` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_38\sa_ep1_38.questphase` / h7 / 382 -> 392 -> 354 |
| `1553ea49805c9d5b4f24` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_38\sa_ep1_38.questphase` / h7 / 347 -> 345 -> 346 |
| `181f231b641eba46ad3b` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_38\sa_ep1_38.questphase` / h271 / 27 -> 3 -> 26 |
| `2165c31c38fd80af8cdc` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_38\sa_ep1_38.questphase` / h271 / 39 -> 40 -> 37 |
| `2734b8ca598133b05e14` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_38\sa_ep1_38.questphase` / h7 / 434 -> 436 -> 340 |
| `2765fcbe8f4e745fbc8e` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_38\sa_ep1_38.questphase` / h271 / 28 -> 33 -> 35 |
| `27989a991fbce5b0fc5c` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_38\sa_ep1_38.questphase` / h7 / 414 -> 368 -> 367 |
| `2f5e3055753dc4c41645` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_38\sa_ep1_38.questphase` / h271 / 40 -> 37 -> 12 |
| `2fb18be6f0f0cc83eee7` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_38\sa_ep1_38.questphase` / h271 / 33 -> 35 -> 25 |
| `3aaa77554027632f87e9` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_38\sa_ep1_38.questphase` / h7 / 407 -> 357 -> 391 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
