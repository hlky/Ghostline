# ep1-sa-ep1-37

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\sandbox_activities\sa_ep1_37\community\sa_ep1_37_av_com.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_37\community\sa_ep1_37_enemies_com_01.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_37\community\sa_ep1_37_enemies_com_02.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_37\community\sa_ep1_37_var_01_com.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_37\community\sa_ep1_37_var_01_custom_com.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_37\community\sa_ep1_37_var_02_com.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_37\community\sa_ep1_37_var_02_reinforcement_com.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_37\sa_ep1_37.gamedef` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_37\sa_ep1_37.quest` | content candidate | 1 / 0 | ep1\openworld\sandbox_activities\sa_ep1_30\scenes\sa_ep1_30_chicken_test.scene; ep1\openworld\sandbox_activities\sa_ep1_37\sa_ep1_37.questphase |
| `ep1\openworld\sandbox_activities\sa_ep1_37\sa_ep1_37.questphase` | content candidate | 9 / 0 |  |

## Journal paths observed in these resources

- `ep1/quests/main_quest/q302_reed/06_basketball/03_elevator`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioEventNodeType]` | 12 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 2 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 4 |
| `questCharacterManagerNodeDefinition[questCharacterManagerVisuals_ChangeEntityAppearance,questCharacterManagerVisuals_EntityAppearanceOperationBaseEntityAppearanceEntry,questCharacterManagerVisuals_NodeType]` | 3 |
| `questCheckpointNodeDefinition` | 3 |
| `questCombatNodeDefinition` | 17 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 10 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 6 |
| `questCutControlNodeDefinition` | 3 |
| `questEntityManagerNodeDefinition[questEntityManagerToggleComponent_NodeType,questEntityManagerToggleComponent_NodeTypeParams]` | 5 |
| `questEventManagerNodeDefinition` | 15 |
| `questFXManagerNodeDefinition[questPlayFX_NodeType,questPlayFX_NodeTypeParams]` | 16 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 28 |
| `questInputNodeDefinition` | 13 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 10 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 6 |
| `questItemManagerNodeDefinition[questReInitContainers_NodeType,questReInitContainers_NodeTypeParams]` | 2 |
| `questLogicalAndNodeDefinition` | 7 |
| `questLogicalHubNodeDefinition` | 14 |
| `questLogicalXorNodeDefinition` | 5 |
| `questMiscAICommandNode` | 4 |
| `questOutputNodeDefinition` | 13 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 5 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam,questLogicalCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 12 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 4 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questNodeLoadingCondition]` | 2 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 19 |
| `questPauseConditionNodeDefinition[questTickDelay_ConditionType,questTimeCondition]` | 4 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 16 |
| `questPhaseNodeDefinition` | 9 |
| `questRandomizerNodeDefinition` | 2 |
| `questSceneNodeDefinition[scnWorldMarker]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 39 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 6 |
| `questStartNodeDefinition` | 1 |
| `questSwitchNodeDefinition[questConditionItem,questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questTransformAnimatorNodeDefinition[questTransformAnimatorNode_Action_Play]` | 1 |
| `questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]` | 1 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 4 |
| `questVehicleNodeDefinition[questMoveOnSpline_NodeType]` | 6 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 13 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 10 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `a5f6ff0df46f7043f2b5` | 7 | `ep1\openworld\sandbox_activities\sa_ep1_37\sa_ep1_37.questphase` / h7 / 269 -> 270 -> 285 |
| `05c7a2151e0cd17400d5` | 6 | `ep1\openworld\sandbox_activities\sa_ep1_37\sa_ep1_37.questphase` / h541 / 26 -> 30 -> 3 |
| `329f0e4d8dbc227b5494` | 6 | `ep1\openworld\sandbox_activities\sa_ep1_37\sa_ep1_37.questphase` / h7 / 368 -> 319 -> 260 |
| `3e6653e916afcf7cc2e1` | 6 | `ep1\openworld\sandbox_activities\sa_ep1_37\sa_ep1_37.questphase` / h541 / 26 -> 30 -> 21 |
| `fc910f43d5ff9aabecc6` | 6 | `ep1\openworld\sandbox_activities\sa_ep1_37\sa_ep1_37.questphase` / h541 / 2 -> 26 -> 30 |
| `120c5c4bbfcbfae70bc4` | 5 | `ep1\openworld\sandbox_activities\sa_ep1_37\sa_ep1_37.questphase` / h1687 / 386 -> 385 -> 387 |
| `402758845f86d6dd89dc` | 5 | `ep1\openworld\sandbox_activities\sa_ep1_37\sa_ep1_37.questphase` / h749 / 8 -> 13 -> 14 |
| `e239bb3187912262f96a` | 5 | `ep1\openworld\sandbox_activities\sa_ep1_37\sa_ep1_37.questphase` / h749 / 4 -> 11 -> 3 |
| `20a77143a898bc753a26` | 4 | `ep1\openworld\sandbox_activities\sa_ep1_37\sa_ep1_37.questphase` / h986 / 249 -> 344 -> 372 |
| `9890c704bd8503fd1750` | 4 | `ep1\openworld\sandbox_activities\sa_ep1_37\sa_ep1_37.questphase` / h749 / 13 -> 14 -> 15 |
| `cb15f618f342a00de266` | 4 | `ep1\openworld\sandbox_activities\sa_ep1_37\sa_ep1_37.questphase` / h1687 / 400 -> 391 -> 392 |
| `01cc762cd06f16743b1c` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_37\sa_ep1_37.questphase` / h7 / 247 -> 327 -> 231 |
| `0307c8e1c2bd71322d7d` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_37\sa_ep1_37.questphase` / h7 / 340 -> 265 -> 379 |
| `0672ae8d2fae884916ec` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_37\sa_ep1_37.questphase` / h7 / 246 -> 325 -> 249 |
| `099a259d14720a1f55dc` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_37\sa_ep1_37.questphase` / h7 / 332 -> 392 -> 247 |
| `0e0287304116817479f5` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_37\sa_ep1_37.questphase` / h7 / 265 -> 379 -> 325 |
| `0f6060800f34fba21084` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_37\sa_ep1_37.questphase` / h7 / 337 -> 340 -> 265 |
| `1553ea49805c9d5b4f24` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_37\sa_ep1_37.questphase` / h7 / 253 -> 251 -> 252 |
| `181f231b641eba46ad3b` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_37\sa_ep1_37.questphase` / h541 / 30 -> 3 -> 29 |
| `2165c31c38fd80af8cdc` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_37\sa_ep1_37.questphase` / h541 / 41 -> 42 -> 38 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
