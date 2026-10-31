# ep1-sa-ep1-39

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\sandbox_activities\sa_ep1_39\communities\sa_ep1_39_av_com.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_39\communities\sa_ep1_39_kurt_com.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_39\communities\sa_ep1_39_kurtz_reinforcement.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_39\communities\sa_ep1_39_var_01_com.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_39\communities\sa_ep1_39_var_02_com.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_39\communities\sa_ep1_39_voodoo_com.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_39\sa_ep1_39.gamedef` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_39\sa_ep1_39.quest` | content candidate | 1 / 0 | ep1\openworld\sandbox_activities\sa_ep1_30\scenes\sa_ep1_30_chicken_test.scene; ep1\openworld\sandbox_activities\sa_ep1_39\sa_ep1_39.questphase |
| `ep1\openworld\sandbox_activities\sa_ep1_39\sa_ep1_39.questphase` | content candidate | 9 / 0 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioEventNodeType]` | 12 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 2 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 4 |
| `questCharacterManagerNodeDefinition[questCharacterManagerVisuals_ChangeEntityAppearance,questCharacterManagerVisuals_EntityAppearanceOperationBaseEntityAppearanceEntry,questCharacterManagerVisuals_NodeType]` | 3 |
| `questCheckpointNodeDefinition` | 3 |
| `questCombatNodeDefinition` | 54 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 5 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 7 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 6 |
| `questCutControlNodeDefinition` | 3 |
| `questEntityManagerNodeDefinition[questEntityManagerToggleComponent_NodeType,questEntityManagerToggleComponent_NodeTypeParams]` | 3 |
| `questEventManagerNodeDefinition` | 11 |
| `questFXManagerNodeDefinition[questPlayFX_NodeType,questPlayFX_NodeTypeParams]` | 12 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 25 |
| `questInputNodeDefinition` | 12 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 8 |
| `questItemManagerNodeDefinition[questReInitContainers_NodeType,questReInitContainers_NodeTypeParams]` | 2 |
| `questLogicalAndNodeDefinition` | 4 |
| `questLogicalHubNodeDefinition` | 9 |
| `questLogicalXorNodeDefinition` | 4 |
| `questMiscAICommandNode` | 14 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 4 |
| `questOutputNodeDefinition` | 12 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam,questLogicalCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 10 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 3 |
| `questPauseConditionNodeDefinition[questNodeLoadingCondition]` | 2 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 18 |
| `questPauseConditionNodeDefinition[questSpawnerCondition,questSpawnerReady_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questTickDelay_ConditionType,questTimeCondition]` | 3 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 16 |
| `questPhaseNodeDefinition` | 9 |
| `questRandomizerNodeDefinition` | 2 |
| `questSceneNodeDefinition[scnWorldMarker]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 48 |
| `questStartNodeDefinition` | 1 |
| `questSwitchNodeDefinition[questConditionItem,questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questVehicleNodeDefinition[questMoveOnSpline_NodeType]` | 6 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 8 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `20a77143a898bc753a26` | 10 | `ep1\openworld\sandbox_activities\sa_ep1_39\sa_ep1_39.questphase` / h7 / 376 -> 374 -> 489 |
| `95b7458b3ffd83fd4357` | 10 | `ep1\openworld\sandbox_activities\sa_ep1_39\sa_ep1_39.questphase` / h1160 / 365 -> 470 -> 471 |
| `05c7a2151e0cd17400d5` | 6 | `ep1\openworld\sandbox_activities\sa_ep1_39\sa_ep1_39.questphase` / h659 / 26 -> 30 -> 3 |
| `3e6653e916afcf7cc2e1` | 6 | `ep1\openworld\sandbox_activities\sa_ep1_39\sa_ep1_39.questphase` / h659 / 26 -> 30 -> 21 |
| `e6a74d0120b15ec0f02c` | 6 | `ep1\openworld\sandbox_activities\sa_ep1_39\sa_ep1_39.questphase` / h7 / 410 -> 508 -> 511 |
| `fc910f43d5ff9aabecc6` | 6 | `ep1\openworld\sandbox_activities\sa_ep1_39\sa_ep1_39.questphase` / h659 / 2 -> 26 -> 30 |
| `120c5c4bbfcbfae70bc4` | 4 | `ep1\openworld\sandbox_activities\sa_ep1_39\sa_ep1_39.questphase` / h1640 / 512 -> 511 -> 513 |
| `22090fb8719a84a4c1f4` | 4 | `ep1\openworld\sandbox_activities\sa_ep1_39\sa_ep1_39.questphase` / h1640 / 514 -> 518 -> 526 |
| `402758845f86d6dd89dc` | 4 | `ep1\openworld\sandbox_activities\sa_ep1_39\sa_ep1_39.questphase` / h941 / 3 -> 11 -> 5 |
| `7787bd2947640f7916d8` | 4 | `ep1\openworld\sandbox_activities\sa_ep1_39\sa_ep1_39.questphase` / h823 / 2 -> 10 -> 8 |
| `d689f459710d85cd37d6` | 4 | `ep1\openworld\sandbox_activities\sa_ep1_39\sa_ep1_39.questphase` / h1640 / 511 -> 529 -> 514 |
| `e239bb3187912262f96a` | 4 | `ep1\openworld\sandbox_activities\sa_ep1_39\sa_ep1_39.questphase` / h941 / 14 -> 15 -> 16 |
| `f89bc035d6c0e83fa340` | 4 | `ep1\openworld\sandbox_activities\sa_ep1_39\sa_ep1_39.questphase` / h1640 / 529 -> 514 -> 518 |
| `00c3ca0ac0b55db639ca` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_39\sa_ep1_39.questphase` / h7 / 373 -> 376 -> 374 |
| `01cc762cd06f16743b1c` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_39\sa_ep1_39.questphase` / h7 / 375 -> 469 -> 362 |
| `0307c8e1c2bd71322d7d` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_39\sa_ep1_39.questphase` / h7 / 487 -> 408 -> 507 |
| `0f6060800f34fba21084` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_39\sa_ep1_39.questphase` / h7 / 472 -> 487 -> 408 |
| `10928bf3a09bffffa44f` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_39\sa_ep1_39.questphase` / h7 / 361 -> 468 -> 363 |
| `1553ea49805c9d5b4f24` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_39\sa_ep1_39.questphase` / h7 / 386 -> 383 -> 384 |
| `181f231b641eba46ad3b` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_39\sa_ep1_39.questphase` / h659 / 30 -> 3 -> 29 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
